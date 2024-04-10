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
def busqueda_amplitud(mundo, inicio, objetivo):
    # Convertir el estado inicial y objetivo en nodos
    nodo_inicio = Nodo(inicio)
    nodo_objetivo = Nodo(objetivo)

    # Inicializar la cola de nodos a explorar
    cola = [nodo_inicio]

    # Inicializar conjunto de nodos visitados
    visitados = set()

    # Inicializar contador de nodos expandidos y profundidad máxima
    nodos_expandidos = 0
    profundidad_maxima = 0

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
            return camino[::-1], nodos_expandidos, profundidad_maxima  # Devolver el camino invertido, nodos expandidos y profundidad máxima

        # Agregar el nodo actual al conjunto de nodos visitados
        visitados.add(nodo_actual.estado)

        # Obtener los sucesores del nodo actual
        sucesores = obtener_sucesores(mundo, nodo_actual)

        # Agregar los sucesores no visitados a la cola
        for sucesor in sucesores:
            if sucesor.estado not in visitados and sucesor not in cola:  # Verificar si el sucesor no ha sido visitado ni está en la cola
                cola.append(sucesor)

    # Si no se encuentra el objetivo, devolver None para el camino y la profundidad
    return None, nodos_expandidos, profundidad_maxima

# Función para cargar el mundo desde un archivo txt y encontrar la posición inicial y la meta
def cargar_mundo_y_encontrar_posiciones(archivo):
    mundo = []
    inicio = None
    objetivo = None
    with open(archivo, 'r') as f:
        for i, line in enumerate(f):
            row = list(map(int, line.strip().split()))
            mundo.append(row)
            for j, cell in enumerate(row):
                if cell == 2:  # Si encontramos el inicio
                    inicio = (i, j)
                elif cell == 5:  # Si encontramos la meta
                    objetivo = (i, j)
    return mundo, inicio, objetivo

# Función principal para probar el algoritmo
def main(archivo):
    # Cargar el mundo desde el archivo y encontrar la posición inicial y la meta
    mundo, inicio, objetivo = cargar_mundo_y_encontrar_posiciones(archivo)

    # Ejecutar el algoritmo de búsqueda en amplitud
    camino, nodos_expandidos, profundidad_maxima = busqueda_amplitud(mundo, inicio, objetivo)

    # Mostrar el resultado
    if camino:
        print("Camino encontrado:", camino)
        print("Nodos expandidos:", nodos_expandidos)
        print("Profundidad del arbol:", profundidad_maxima)
    else:
        print("No se encontró un camino.")

if __name__ == "__main__":
    archivo = "prueba1.txt"  # Nombre del archivo que contiene la descripción del mundo
    main(archivo)
