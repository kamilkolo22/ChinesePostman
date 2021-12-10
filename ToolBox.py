from copy import deepcopy


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


def print_graph(graph):
    """Wypisuje graf jako slownik pythona"""
    for v in graph:
        print(v, ":", end="")
        for u in graph[v]:
            print(" ", u, end="")
        print("")


def check_euler(graph):
    for v in graph:
        if len(graph[v]) % 2:
            return False
    return True


def dfs_euler(graph, v, path=None):
    if path is None:
        graph = deepcopy(graph)
        path = []

    for neighbor in graph[v]:  # u jeszce nie odwiedzony
        print(graph)
        graph[v].remove(neighbor)
        graph[neighbor].remove(v)
        print(graph)
        dfs_euler(graph, neighbor, path)
    path.append(v)
    return path
