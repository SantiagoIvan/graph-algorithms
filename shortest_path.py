from undirected_path import build_graph_from_incidence_matrix
import time

edges = [["w", "x"], ["x", "y"], ["z", "y"], ["z", "v"], ["w", "v"]]

my_graph = build_graph_from_incidence_matrix(edges)

# Necesitaria un vector de visitados, para no volver a analizar un nodo ya visto
# Aplicar un Breadthfirst seria mas conveniente, debido a que es mejor analizar por niveles
# si el buscado esta ahi, en lugar de ir hasta el fondo, donde ya la longitud se me va al carajo
# si en el nivel n encuentro al buscado, ese sera el camino de longitud mas corta

# ESTO ES SUPONIENDO QUE TODAS LAS ARISTAS POSEEN EL MISMO PESO
# en este caso ni estoy teniendo en cuenta el peso


def build_path(vector, init):
    (current, distance, prev) = init
    path = [current]
    while prev:
        path.append(prev)
        for elem in vector:
            if elem[0] == prev:
                prev = elem[2]
                break
    path.reverse()
    return path


def node_visited(node, visited):
    for elem in visited:
        if elem[0] == node:
            return True
    return False


def shortest_path(graph, start, end):
    visited = set([(start, 0, None)])
    # de esta forma, el que tiene None, es el comienzo, y cuando encuentro
    # el nodo destino, puedo recorrer este vector armando el path con el tercer elemento, ya que se quienes
    # son los ancestros de un nodo en un camino

    queue = []
    # trio ordenado, (x, distance, prev), siendo x el nodo actual y prev, el precesor

    queue.append((start, 0, None))  # None porque nadie es el padre de este

    while len(queue) > 0:
        (current, distance, prev) = queue.pop(0)

        if current == end:
            path = build_path(visited, (current, distance, prev))
            return (distance, path)
        for adj in graph[current]:
            if not node_visited(adj, visited):
                visited.add((adj, distance + 1, current))
                queue.append((adj, distance + 1, current))
    print("Those nodes are not connected")


print(shortest_path(my_graph, "w", "v"))
