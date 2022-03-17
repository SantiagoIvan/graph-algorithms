# Breadth-First Search

# Recorrer el arbol por nivel

# Para ello, necesito:
# - una cola
# - por cada nodo que proceso, meto en la cola a todos sus hijos
# - Luego de procesar al nodo, (que en este caso sera meterlo en una lista de resultados para printearlo)
# repito el proceso de forma iterativa con cada uno de los nodos que hay en la cola
# Sigo iterando hasta que la cola queda vacia

# Recordemos que la cola es una estructura de dato donde FIFO, first in, first out.

# Si quisiera hacer el deepthfirst search de forma iterativa, debería usar una pila,
# cosa de meter el hijo izquierdo de cada nodo en la pila primero y hacer un pop.



# Sea graph =
my_graph = {
    "a": ["b", "d"],
    "b": ["c"],
    "c": [],
    "d": ["b", "f"],
    "e": ["d"],
    "f": []
}

def breadthfirst_search(graph, node):
    queue = []
    result = []

    if not node: return []
    queue.append(node)
    while len(queue) > 0:
        # sacar de la cola
        next = queue.pop(0)
        result.append(next.value)
        # agrego a la cola a los adyacentes, siempre y cuando tenga vecinos.
        if node in graph.keys():
            for adj in graph[node]:
                queue.append(adj)
    
    return result   
