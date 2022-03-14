# Breath-First Search

# Recorrer el arbol por nivel

# Para ello, necesito:
# - una cola
# - por cada nodo que proceso, meto en la cola a todos sus hijos
# - Luego de procesar al nodo, (que en este caso sera meterlo en una lista de resultados para printearlo)
# repito el proceso de forma iterativa con cada uno de los nodos que hay en la cola
# Sigo iterando hasta que la cola queda vacia

# Recordemos que la cola es una estructura de dato donde FIFO, first in, first out.

def tree_by_levels(node):
    queue = []
    result = []

    if not node: return []
    queue.append(node)
    while len(queue) > 0:
        # sacar de la cola
        next = queue.pop(0)
        result.append(next.value)
        
        next.left and queue.append(next.left)
        next.right and queue.append(next.right)
    
    return result   
