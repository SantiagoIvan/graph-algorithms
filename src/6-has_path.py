my_graph = {
    "a": ["b", "d"],
    "b": ["c"],
    "c": [],
    "d": ["b", "f"],
    "e": ["d"],
    "f": []
}

# esta version seria aplicando depthfirst, fijate que tomo un camino y voy hasta el fondo, es decir, por el primer vecino, y no cambio hasta que vea que me retorna
def has_path_depthfirst(graph, source, destiny):
    if source == destiny: return True # estoy en el destino asi que retorno True a quien me haya llamado
    if not source: return False
    
    for adj in graph[source]:
        if has_path_depthfirst(graph, adj, destiny): return True # burbujeo el retorno
    
    # Si yo no soy el destino, y ninguno de mis hijos tampoco, retorno False
    return False

  

# he aqui una version iterativa, utilizando una cola, para aplicar breadthfirst
def has_path_breadthfirst( graph, source, destiny):
    queue = []
    if not source: return False
    
    queue.append(source)
    while len(queue)>0:
        next = queue.pop(0) # saco el primer elemento
        if next == destiny: return True
        # si estoy aca, es porque no es el destino, por lo que agrego a la cola a todos sus hijos
        for adj in graph[next]:
            queue.append(adj)
        # analizo en las siguientes iteraciones al siguiente nivel
