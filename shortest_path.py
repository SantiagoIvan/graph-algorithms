from undirected_path import build_graph_from_incidence_matrix

edges = [["w", "x"], ["x", "y"], ["z", "y"], ["z", "v"], ["w", "v"]]

my_graph = build_graph_from_incidence_matrix(edges)

# Necesitaria un vector de visitados, para no volver a analizar un nodo ya visto
# Aplicar un Breadthfirst seria mas conveniente, debido a que es mejor analizar por niveles
# si el buscado esta ahi, en lugar de ir hasta el fondo, donde ya la longitud se me va al carajo
# si en el nivel n encuentro al buscado, ese sera el camino de longitud mas corta

# ESTO ES SUPONIENDO QUE TODAS LAS ARISTAS POSEEN EL MISMO PESO
# en este caso ni estoy teniendo en cuenta el peso


def shortest_path(graph, start, end):
    visited = set([start])
    queue = []  # par ordenado, (x, distance), siendo x el nodo actual

    queue.append((start, 0))

    while len(queue) > 0:
        (next, distance) = queue.pop(0)

        if next == end:
            return distance
        for adj in graph[next]:
            if adj not in visited:
                visited.add(adj)
                queue.append((adj, distance + 1))
    print("Those nodes are not connected")
    return -1


print(shortest_path(my_graph, "w", "z"))
