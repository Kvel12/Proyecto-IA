import time

# Definición de la clase para representar un nodo
class Nodo:
    def __init__(self, estado, padre=None, profundidad=0):
        self.estado = estado
        self.padre = padre
        self.profundidad = profundidad

# Función para obtener los sucesores válidos de un estado
def obtener_sucesores(mundo, nodo, rutas_visitadas):
    sucesores = []
    movimientos = [(1, 0), (-1, 0), (0, 1), (0, -1)]
    for mov in movimientos:
        nuevo_estado = (nodo.estado[0] + mov[0], nodo.estado[1] + mov[1])
        if 0 <= nuevo_estado[0] < len(mundo) and 0 <= nuevo_estado[1] < len(mundo[0]) and mundo[nuevo_estado[0]][nuevo_estado[1]] != 1:
            if nuevo_estado not in rutas_visitadas:
                sucesor = Nodo(nuevo_estado, nodo, nodo.profundidad + 1)
                sucesores.append(sucesor)
                rutas_visitadas.add(nuevo_estado)
    return sucesores

# Función para obtener las coordenadas de inicio y objetivo
def obtener_inicio_objetivo(mundo):
    for i in range(len(mundo)):
        for j in range(len(mundo[0])):
            if mundo[i][j] == 2:
                inicio = (i, j)
            elif mundo[i][j] == 5:
                objetivo = (i, j)
    return inicio, objetivo

# Algoritmo de búsqueda en amplitud
def busqueda_amplitud(mundo):
    start_time = time.time()
    inicio, objetivo = obtener_inicio_objetivo(mundo)
    nodo_inicio = Nodo(inicio)
    nodo_objetivo = Nodo(objetivo)
    cola = [nodo_inicio]
    rutas_visitadas = set()
    rutas_visitadas.add(nodo_inicio.estado)
    nodos_expandidos = 0
    profundidad_maxima = 0
    nombre = "Búsqueda por Amplitud"

    while cola:
        nodo_actual = cola.pop(0)
        nodos_expandidos += 1
        profundidad_maxima = max(profundidad_maxima, nodo_actual.profundidad)

        if nodo_actual.estado == nodo_objetivo.estado:
            camino = []
            while nodo_actual:
                camino.append(nodo_actual.estado)
                nodo_actual = nodo_actual.padre
            end_time = time.time()
            computation_time = end_time - start_time
            return camino[::-1], nodos_expandidos, profundidad_maxima, computation_time, nombre

        sucesores = obtener_sucesores(mundo, nodo_actual, rutas_visitadas)
        cola.extend(sucesores)

    end_time = time.time()
    computation_time = end_time - start_time
    return None, nodos_expandidos, profundidad_maxima, computation_time