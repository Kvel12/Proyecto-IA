import time

def profundidad_evitando_ciclos(world_data):
    # Iniciar el temporizador para medir el tiempo de cómputo del algoritmo de búsqueda
    start_time = time.perf_counter()

    # Función interna para expandir el nodo actual en la búsqueda
    def expand(node):
        # Incrementar el contador de nodos expandidos
        nonlocal nodes_expanded
        nodes_expanded += 1

        # Extraer la posición y el camino del nodo actual
        x, y, path = node

        # Iterar sobre las posibles direcciones de movimiento en el orden indicado: derecha, abajo, izquierda, arriba
        for dx, dy in [(1, 0), (0, 1), (-1, 0), (0, -1)]:
            # Calcular la nueva posición a partir de la dirección de movimiento
            nx, ny = x + dx, y + dy

            # Verificar si la posición resultante está dentro de los límites del mundo y es válida para moverse (es decir, no es una pared ni una posición ya visitada)
            # Si la posición es válida, se expande recursivamente desde la nueva posición
            if 0 <= nx < 10 and 0 <= ny < 10 and (nx, ny) not in path and world_data[ny][nx] != 1:
                # Agregar la nueva posición al camino actual
                new_path = path + [(nx, ny)]

                # Si se encuentra el objetivo, devolver el camino encontrado
                if world_data[ny][nx] == 5:
                    return new_path
                else:
                    # Si no es el objetivo, expandir recursivamente desde la nueva posición
                    result = expand((nx, ny, new_path))
                    if result:
                        return result

        # Si no se encuentra ninguna solución desde este nodo, devolver None
        # Esto provocará que la búsqueda retroceda al nodo anterior y continúe desde allí
        # En otras palabras, se realiza una búsqueda en profundidad evitando ciclos
        return None

    # Inicializar el contador de nodos expandidos y la posición inicial del agente
    nodes_expanded = 0
    start_position = None

    # Encontrar la posición inicial del agente en el mundo
    for y in range(10):
        for x in range(10):
            if world_data[y][x] == 2:
                start_position = (x, y)
                break
        if start_position:
            break

    # Si se encuentra la posición inicial, realizar la búsqueda
    if start_position:
        # Realizar la búsqueda desde la posición inicial
        path = expand((start_position[0], start_position[1], [(start_position[0], start_position[1])]))

        # Calcular la profundidad del árbol (longitud del camino encontrado menos 1 para la posición inicial) y el tiempo de cómputo
        depth = len(path) - 1 if path else 0
        end_time = time.perf_counter()
        computation_time = end_time - start_time
        nombre = "Búsqueda por Profundidad"

        # Devolver el camino encontrado, el número de nodos expandidos, la profundidad del árbol y el tiempo de cómputo
        return path, nodes_expanded, depth, computation_time, nombre
    else:
        # Si no se encuentra la posición inicial, devolver None para indicar que no se encontró solución, además, devolver el número de nodos expandidos, la profundidad del árbol y el tiempo de cómputo (0)
        return None, nodes_expanded, 0, 0, nombre


