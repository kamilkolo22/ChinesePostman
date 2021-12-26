import numpy as np
from copy import deepcopy
from queue import PriorityQueue
from HungarianAlgorithm import hungarian_algorithm
from ToolBox import add_edge, find_odd_degree


def chinese_postman(graph):
    """Metoda rozwiazuje problem chińskiego listonosza dla
    nieskierowanego grafu ważonego"""

    graph = deepcopy(graph)
    # Szukamy wierzchołkow o nieparszystych stopniach i
    # łaczymy je jeśli takie istnieja
    odd_degree = find_odd_degree(graph)
    if len(odd_degree) > 0:
        allocation_matrix = []
        paths = {}
        # Algorytm Dijsktry
        for v in odd_degree:
            dist, pred = Dijkstra(graph, v)
            paths[v] = pred
            allocation_matrix.append([dist[i] for i in odd_degree])

        # Algorytm wegierski do znalezenia optymalnych polaczen
        allocation_matrix = np.array(allocation_matrix, dtype=float)
        np.fill_diagonal(allocation_matrix, np.inf)
        assigned = hungarian_algorithm(allocation_matrix.copy())

        # Pary wierzchołkow ktore bedziemy chcieli polaczyc sciezka
        to_connect = []
        for pair in assigned:
            if not [odd_degree[pair[1]], odd_degree[pair[0]]] in to_connect:
                to_connect.append([odd_degree[pair[0]], odd_degree[pair[1]]])

        # dodajemy sciezki
        for pair in to_connect:
            # Odczytujemy najkrotsza sciezke
            raw_path = paths[pair[0]]
            shortest_path = [pair[1]]
            v = raw_path[pair[1]]
            while True:
                shortest_path.append(v)
                if v == pair[0]:
                    break
                else:
                    v = raw_path[v]

            for i in range(len(shortest_path) - 1):
                # odczytujemy wage dla danej krawedzi
                for w in range(len(graph[shortest_path[i]])):
                    if graph[shortest_path[i]][w][0] == shortest_path[i + 1]:
                        weight = graph[shortest_path[i]][w][1]
                        # Dodajemy krawedz wraz z odpowiednia waga
                add_edge(graph, (shortest_path[i], shortest_path[i + 1]))
                graph[shortest_path[i]][-1] = (shortest_path[i + 1], weight)
                graph[shortest_path[i + 1]][-1] = (shortest_path[i], weight)
    return dfs_euler_w(graph, 'A')


def Dijkstra(wgraph, s):
    """Najkrotsze sciezki miedzy z wierzcholka s"""
    # Init
    dist = {}
    pred = {}
    for v in wgraph:
        dist[v] = np.inf
        pred[v] = None
    dist[s] = 0
    q = PriorityQueue()
    q.put((0, s))
    V = set()  # zbiór wierzchołkow przetworzonych
    while not q.empty():
        (d, u) = q.get()
        if u not in V:
            V.add(u)
            for (v, w) in wgraph[u]:   # relax
                if dist[v] > dist[u] + int(w):
                    dist[v] = dist[u] + int(w)
                    pred[v] = u
                    q.put((dist[v], v))
    return dist, pred


def dfs_euler_w(graph, v, path=None):
    """Znajduje cykl eulera w grafie wazonym"""
    if path is None:
        graph = deepcopy(graph)
        path = []

    if len(graph[v]) > 0:
        for neighbor in graph[v]:  # u jeszce nie odwiedzony
            neighbor = neighbor[0]
            for i in range(len(graph[v])):
                if graph[v][i][0] == neighbor:
                    del graph[v][i]
                    break
            # graph[v].remove(neighbor)
            for i in range(len(graph[neighbor])):
                if graph[neighbor][i][0] == v:
                    del graph[neighbor][i]
                    break
            # graph[neighbor].remove(v)
            dfs_euler_w(graph, neighbor, path)
    path.append(v)
    return path
