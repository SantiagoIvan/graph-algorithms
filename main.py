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

def breadthfirst_search(node):
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

def deepthfirst_search_recursive(node):
    if node:
        print(node.value)
        deepthfirst_search(node.left)
        deepthfirst_search(node.right)
    return

def deepthfirst_search_iterative(node):
    result = []
    stack = []
    
    stack.append(node)
    while node and len(stack) > 0:
        node = stack.pop()
        result.append(node.value)
        node.right and stack.append(node.right)
        node.left and stack.append(node.left)
        
    
    return result
