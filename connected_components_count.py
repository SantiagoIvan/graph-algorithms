# Sea G un grafo no dirigido potencialmente ciclico
# imagen: graph3

# Cuenta cuantos componentes o islas existen en mi grafo.
# No me refiero a clases de equivalencia ya que no tiene por que ser reflexiva o transitiva la relacion.
# De hecho, en la foto se puede ver que no cumple ninguna de esas 2, pero serviria de todas formas

my_graph = {1: [2], 2: [1], 3: [], 4: [6], 5: [6], 6: [4, 5, 7, 8], 7: [6], 8: [6]}

# Enfoque:
# Se que voy a tener un contador de islas inicializado en 0.
# Tambien se que voy a tener que iterar por todos los nodos.
# Y tambien voy a tener que tener un set de nodos visitados, por cada viaje que realice, y voy a
# tener que comparar los sets para ver si los nodos visitados se repiten. Porque si es asi, quiere decir
# que estoy en la misma isla por lo tanto no cuento ese grupo


def depthfirst(graph, node, visited, result):
    if node in visited:
        return []
    visited.add(node)
    result.add(node)
    for adj in graph[node]:
        depthfirst(graph, adj, visited, result)
    return result


def connected_components_count(graph):
    count = 0
    visited = set([])
    array_of_groups = []

    for node in graph.keys():
        if not node in visited:
            aux = depthfirst(graph, node, visited, set([]))
            array_of_groups.append(aux)
            count += 1

    return (count, array_of_groups)


def largest_component_in_graph(graph):
    (_, components) = connected_components_count(graph)
    return max(components, key=len)


# puedo aplicar depth o breadth es lo mismo, para cada uno, y asi recorrer el grafo
# cuando completo un recorrido, marco todos los nodos por los cuales pase como visitados
# y como estoy recorriendo todos los adyacentes de cada nodo ( y es grafo no dirigido)
# yo se que para esos otros nodos, voy a obtener el mismo grupo de elementos
# Por esa razon, el vector de visitados lo tengo aca arriba y no en cada iteracion del depthfirst.
# Uso el mismo vector para todas las iteraciones
# Cuando paso a la siguiente iteracion, pregunto si ese nodo ya lo visite anteriormente,
# si es asi, ya se que recorri todos sus vecinos, y no hara falta aplicar la busqueda desde ese nodo

print(connected_components_count(my_graph))
print("Largest component is ", largest_component_in_graph(my_graph))
