# ---- ENUNCIADO ----
# Tengo un mapa 2D.
# En los casilleros con una L ( land ) es posible pararse
# Los casilleros con una W ( water ) no es posible pararse, no deben ser tenidos en cuenta
# La idea de este ejercicio es contar islas, mostrar sus casilleros y decir cual es la isla mas grande.
# -------------------

# Este mapa en 2D es un grafo no dirigido, por lo que podria armarme una matriz de adyacencia
# a partir del mapa
# Deberia pararme en todos los nodos, contar los componentes y los que ya visite, no visitarlos de nuevo
# Reutilizando el codigo de connected components podria resolver este ejercicio
# Deberia recorrer la grilla, y si encuentro una tierra, aplicar una busqueda desde ese nodo para encontrar
# todos los casilleros de la isla
# Podria armar la matriz de adyacencia, pero es medio al pedo, ya la matriz que me dan es un mapita
# y no voy a recorrer todo el mapa solo para armar esa matriz y luego recorrer la matriz.
# Puedo directamente recorrer el mapa y hallarlos adyacentes de 1, total es moverme a la derecha/izquierda/arriba/abajo


my_map_2d = [
    ["W", "L", "W", "W", "L", "W"],
    ["L", "L", "W", "W", "L", "W"],
    ["W", "L", "W", "W", "W", "W"],
    ["W", "W", "W", "L", "L", "W"],
    ["W", "L", "W", "L", "L", "W"],
    ["W", "W", "W", "W", "W", "W"],
]


def breadthfirst(my_map, start, visited):
    queue = []
    local_visits = set([])
    # para mantener el control de lo que visite en esta iteracion, y retornarlo, ya que contendria
    # a los elementos de esta isla

    queue.append(start)

    while len(queue) > 0:
        (row, col) = queue.pop(0)

        # Restricciones
        if (row, col) in local_visits:
            continue

        rowIsCorrect = 0 <= row and row < len(my_map)
        colIsCorrect = 0 <= col and col < len(my_map[row])
        if (not rowIsCorrect) or (not colIsCorrect) or (my_map[row][col] == "W"):
            continue

        local_visits.add((row, col))
        visited.add((row, col))

        # Agrego los adyacentes, total con el caso base de arriba, si son invalidos quedan descartados del analisis
        queue.append((row - 1, col))
        queue.append((row, col - 1))
        queue.append((row + 1, col))
        queue.append((row, col + 1))

    return local_visits


# queda mas prolijo de esta forma recursiva, ya que con 1 condicional, que seria mi caso base,
# retorno directamente si es una posicion invalida
def depthfirst(my_map, start, visited, local_visits):
    if start in local_visits:
        return
    (row, column) = start
    rowIsCorrect = 0 <= row and row < len(my_map)
    colIsCorrect = 0 <= column and column < len(my_map[row])

    if (not rowIsCorrect) or (not colIsCorrect) or (my_map[row][column] == "W"):
        return

    local_visits.add((row, column))
    visited.add((row, column))

    # visito a los adyacentes
    depthfirst(my_map, (row - 1, column), visited, local_visits)
    depthfirst(my_map, (row, column - 1), visited, local_visits)
    depthfirst(my_map, (row + 1, column), visited, local_visits)
    depthfirst(my_map, (row, column + 1), visited, local_visits)

    return local_visits


# retorna la cantidad de islas, y su composicion
def count_islands(my_map):
    count = 0
    visited = set([])
    # set de pares ordenados, representando las coordenadas de las tierras visitadas
    # las W las tendria que ignorar de todo analisis, ni las deberia visitar
    islands = []

    for row in range(len(my_map)):
        for column in range(len(my_map[row])):
            if my_map[row][column] == "W":
                continue  # ignoro el agua
            # si es L, aplico una busqueda, cualquiera, es lo mismo, depth o breadth
            if (row, column) not in visited:
                island = breadthfirst(my_map, (row, column), visited)
                # island = depthfirst(my_map, (row, column), visited, set([]))
                islands.append(island)
                count += 1
    return (count, islands)


def longest_island(islands):
    return max(islands, key=len)


(q, islands) = count_islands(my_map_2d)
print("Cantidad de islas: ", q)
print("Casilleros de cada isla: ", islands)
print("Isla mas larga: ", longest_island(islands))
