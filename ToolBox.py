# Funkcje z zajęć oraz kilka funkcji pomocniczych

def add_vertex(graph, vertex):
    """Nowy wierzcholek do istniejacego grafu"""
    if vertex not in graph:
        graph[vertex] = []


def add_edge(graph, edge):
    """Dodaje krawedz do grafu"""
    u, v = edge
    add_vertex(graph, u)
    add_vertex(graph, v)
    if u == v:
        raise ValueError("pętla!")
    if v not in graph[u]:
        graph[u].append(v)
    if u not in graph[v]:
        graph[v].append(u)


def add_arc(graph, arc):
    """Dodaje nowy luk, graf prosty skierowany"""
    u, v = arc
    add_vertex(graph, u)
    add_vertex(graph, v)
    if v not in graph[u]:
        graph[u].append(v)


def print_graph(graph):
    """Wypisuje graf jako slownik pythona"""
    for v in graph:
        print(v, ":", end="")
        for u in graph[v]:
            print(" ", u, end="")
        print("")


def graph_from_edges(filename, directed=False):
    """Wczytuję graf z pliku tesktowego, który w każdej lini
    zawiera opis jednej krawędzi oraz waga danej krawedzi"""
    graph = {}
    with open(filename, 'r') as f:
        for line in f:
            words = line.split()
            if len(words) == 1:
                add_vertex(graph, words[0])
            elif len(words) == 2:
                if directed:
                    add_arc(graph, (words[0], words[1]))
                else:
                    add_edge(graph, (words[0], words[1]))
            elif len(words) >= 3:
                if directed:
                    add_arc(graph, (words[0], words[1]))
                    graph[words[0]][-1] = (words[1], words[2])
                else:
                    add_edge(graph, (words[0], words[1]))
                    graph[words[0]][-1] = (words[1], words[2])
                    graph[words[1]][-1] = (words[0], words[2])
    return graph


def find_odd_degree(graph):
    degrees = odd_vertexes_degree(graph)
    graph_l = list(graph)
    vertexes = []
    for i in range(len(graph)):
        if degrees[i]:
            vertexes.append(graph_l[i])
    return vertexes


def check_euler(graph):
    odd_degree = odd_vertexes_degree(graph)
    if sum(odd_degree):
        return False
    else:
        return True


def odd_vertexes_degree(graph):
    """Sprawdze ile jest wierzcholkow nieparzystych"""
    odd_degree = []
    for v in graph:
        if len(graph[v]) % 2:
            odd_degree.append(1)
        else:
            odd_degree.append(0)
    return odd_degree
