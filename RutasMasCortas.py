# Problema: Encontrar la ruta más corta entre dos ciudades (nodos) en un mapa (grafo) con distancias.
# Usamos un diccionario para decir qué ciudades están conectadas y cuánto "cuesta" (distancia) ir de una a otra.

import heapq  # Esto nos ayuda a elegir siempre la ciudad con la menor distancia acumulada.

def dijkstra(grafo, inicio, fin):
    # grafo: un diccionario que dice qué ciudades están conectadas y las distancias.
    # inicio: la ciudad donde empezamos (ejemplo: 'A').
    # fin: la ciudad a la que queremos llegar (ejemplo: 'D').

    # Creamos un diccionario para guardar las distancias más cortas desde 'inicio' a cada ciudad.
    distancias = {ciudad: float('inf') for ciudad in grafo}  # Todas las distancias empiezan en "infinito".
    distancias[inicio] = 0  # La distancia desde el inicio a sí mismo es 0.

    # Guardamos de dónde venimos para cada ciudad, para reconstruir el camino después.
    anteriores = {ciudad: None for ciudad in grafo}

    # Usamos una cola de prioridad para explorar las ciudades, empezando por la más cercana.
    cola = [(0, inicio)]  # (distancia, ciudad). Empezamos con la ciudad inicial y distancia 0.

    # Mientras haya ciudades por explorar:
    while cola:
        # Sacamos la ciudad con la menor distancia acumulada.
        distancia_actual, ciudad_actual = heapq.heappop(cola)

        # Si llegamos a la ciudad final, terminamos.
        if ciudad_actual == fin:
            break

        # Miramos todas las ciudades vecinas de la ciudad actual.
        for vecina, peso in grafo[ciudad_actual].items():
            # Calculamos la distancia para llegar a la vecina pasando por la ciudad actual.
            nueva_distancia = distancia_actual + peso

            # Si esta nueva distancia es menor que la que ya teníamos, la actualizamos.
            if nueva_distancia < distancias[vecina]:
                distancias[vecina] = nueva_distancia
                anteriores[vecina] = ciudad_actual  # Guardamos que vinimos de ciudad_actual.
                heapq.heappush(cola, (nueva_distancia, vecina))  # Añadimos la vecina a la cola.

    # Construimos el camino desde la ciudad final hasta la inicial.
    camino = []
    ciudad_actual = fin
    while ciudad_actual is not None:
        camino.append(ciudad_actual)
        ciudad_actual = anteriores[ciudad_actual]
    camino.reverse()  # Damos la vuelta al camino para que vaya de inicio a fin.

    # Devolvemos la distancia total y el camino. Si no hay camino, devolvemos None.
    return distancias[fin], camino if distancias[fin] != float('inf') else None

# Ejemplo de uso
# Definimos el mapa como un diccionario. Cada ciudad tiene una lista de vecinas y las distancias.
grafo = {
    'A': {'B': 4, 'C': 2},
    'B': {'A': 4, 'C': 1, 'D': 5},
    'C': {'A': 2, 'B': 1, 'D': 8},
    'D': {'B': 5, 'C': 8}
}

# Buscamos el camino más corto de A a D.
distancia, camino = dijkstra(grafo, 'A', 'D')

# Mostramos el resultado.
print(f"La distancia más corta de A a D es: {distancia}")
print(f"El camino es: {' -> '.join(camino)}")

# Explicación del mapa:
# - Desde A puedes ir a B (distancia 4) o a C (distancia 2).
# - Desde B puedes ir a A (4), C (1), o D (5).
# - Desde C puedes ir a A (2), B (1), o D (8).
# - Desde D puedes ir a B (5) o C (8).
# El algoritmo encuentra que el camino más corto es A -> C -> D, con distancia 10.