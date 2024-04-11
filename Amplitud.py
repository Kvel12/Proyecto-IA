import time

# Definición de la clase para representar un nodo en el grafo
class Nodo:
    def __init__(self, estado, padre=None, profundidad=0):
        self.estado = estado
        self.padre = padre
        self.profundidad = profundidad

# Función para obtener los sucesores válidos de un estado
def obtener_sucesores(mundo, nodo):
    sucesores = []
    movimientos = [(1, 0), (-1, 0), (0, 1), (0, -1)]  # Movimientos posibles: abajo, arriba, derecha, izquierda
    for mov in movimientos:
        nuevo_estado = (nodo.estado[0] + mov[0], nodo.estado[1] + mov[1])
        if 0 <= nuevo_estado[0] < len(mundo) and 0 <= nuevo_estado[1] < len(mundo[0]) and mundo[nuevo_estado[0]][nuevo_estado[1]] != 1:
            sucesores.append(Nodo(nuevo_estado, nodo, nodo.profundidad + 1))  # Incrementar la profundidad
    return sucesores

# Algoritmo de búsqueda en amplitud
def busqueda_amplitud(mundo):
    # Encontrar las coordenadas de inicio y destino
    start_x, start_y = None, None
    target_x, target_y = None, None
    for y in range(len(mundo)):
        for x in range(len(mundo[0])):
            if mundo[y][x] == 2:
                start_x, start_y = x, y
            elif mundo[y][x] == 5:
                target_x, target_y = x, y

    # Convertir el estado inicial y objetivo en nodos
    nodo_inicio = Nodo((start_x, start_y))
    nodo_objetivo = Nodo((target_x, target_y))

    # Inicializar la cola de nodos a explorar
    cola = [nodo_inicio]

    # Inicializar conjunto de nodos visitados
    visitados = set()

    # Inicializar contador de nodos expandidos y profundidad máxima
    nodos_expandidos = 0
    profundidad_maxima = 0

    # Inicializar el tiempo de cómputo
    start_time = time.perf_counter()

    # Bucle principal de búsqueda
    while cola:
        # Extraer el nodo de la cola
        nodo_actual = cola.pop(0)

        # Incrementar el contador de nodos expandidos
        nodos_expandidos += 1

        # Actualizar la profundidad máxima
        profundidad_maxima = max(profundidad_maxima, nodo_actual.profundidad)

        # Verificar si el nodo actual es el objetivo
        if nodo_actual.estado == nodo_objetivo.estado:
            # Reconstruir el camino desde el nodo objetivo hasta el inicial
            camino = []
            while nodo_actual:
                camino.append(nodo_actual.estado)
                nodo_actual = nodo_actual.padre
            end_time = time.perf_counter()
            computation_time = end_time - start_time
            return camino[::-1], nodos_expandidos, profundidad_maxima, computation_time  # Devolver el camino invertido, nodos expandidos, profundidad máxima y tiempo de cómputo

        # Agregar el nodo actual al conjunto de nodos visitados
        visitados.add(nodo_actual.estado)

        # Obtener los sucesores del nodo actual
        sucesores = obtener_sucesores(mundo, nodo_actual)

        # Agregar los sucesores no visitados a la cola
        for sucesor in sucesores:
            if sucesor.estado not in visitados and sucesor not in cola:  # Verificar si el sucesor no ha sido visitado ni está en la cola
                cola.append(sucesor)

    # Si no se encuentra el objetivo, devolver None para el camino, la profundidad y el tiempo de cómputo
    end_time = time.perf_counter()
    computation_time = end_time - start_time
    return None, nodos_expandidos, profundidad_maxima, computation_time

