edges = [["i", "j"], ["k", "i"], ["k", "j"], ["m", "k"], ["k", "l"], ["o", "n"]]
# matriz de incidencia

# construyo mi matriz de adyacencia a partir de la matriz de incidencia
# Time complexity = O ( e ).
# Crece linealmente segun el numero de aristas que tenga en el peor de los casos, porque pasare por
# todas las aristas una vez como maximo.

# Space complexity = O ( n )
def build_graph_from_incidence_matrix(matrix):
    my_graph = {}
    for pair in matrix:
        if pair[0] not in my_graph.keys():
            my_graph[pair[0]] = set([pair[1]])
        else:
            my_graph[pair[0]].add(pair[1])
        if pair[1] not in my_graph.keys():
            my_graph[pair[1]] = set([pair[0]])
        else:
            my_graph[pair[1]].add(pair[0])

    return my_graph


my_graph = build_graph_from_incidence_matrix(edges)

# Como hallar un camino entre nodos en un grafo ciclico?
# marcando los nodos que voy visitando como visitados


def has_undirected_path(graph, src, dst, visited=[]):

    if src in visited:
        return False
    print(src)
    visited.append(src)

    if src == dst:
        return True
    for adj in graph[src]:
        if has_undirected_path(graph, adj, dst):
            return True
    return False
