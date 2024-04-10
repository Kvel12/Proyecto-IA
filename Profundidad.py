import time

def profundidad_evitando_ciclos(world_data):

    # Iniciar el temporizador para medir el tiempo de cómputo 
    start_time = time.perf_counter()

    # Función interna para expandir el nodo actual en la búsqueda 
    def expand(node):

        # Incrementar el contador de nodos expandidos 
        nonlocal nodes_expanded
        nodes_expanded += 1
        x, y, path = node

        # Iterar sobre las posibles direcciones de movimiento en ese orden: abajo, derecha, arriba, izquierda
        for dx, dy in [(-1, 0), (0, 1), (1, 0), (0, -1)]:
            nx, ny = x + dx, y + dy

            # Verificar si la posición resultante está dentro de los límites del mundo y es válida
            if 0 <= nx < 10 and 0 <= ny < 10 and (nx, ny) not in path and world_data[ny][nx] != 1:

                # Si se encuentra el objetivo, devolver el camino
                if world_data[ny][nx] == 5:
                    return path + [(nx, ny)]

                # Si no es el objetivo, expandir recursivamente desde la nueva posición
                else:
                    result = expand((nx, ny, path + [(nx, ny)]))
                    if result:
                        return result
                    
        # Si no se encuentra ninguna solución desde este nodo, devolver None
        return None
    
    # Inicializar el contador de nodos expandidos
    nodes_expanded = 0
    start_position = None

    # Encontrar la posición inicial de "agente"
    for y in range(10):
        for x in range(10):
            if world_data[y][x] == 2:
                start_position = (x, y)
                break

        ## Si se encuentra la posición inicial, realizar la búsqueda
        if start_position:
            break
    
    if start_position:
        # Realizar la búsqueda en profundidad evitando ciclos
        path = expand((start_position[0], start_position[1], [start_position]))

        # Calcular la profundidad del árbol (longitud del camino) y el tiempo de cómputo
        depth = len(path) if path else 0
        end_time = time.perf_counter()
        computation_time = end_time - start_time

        # Devolver el camino encontrado, el número de nodos expandidos, la profundidad del árbol y el tiempo de cómputo
        return path, nodes_expanded, depth, computation_time
    else:
        # Si no se encuentra la posición inicial, devolver None para indicar que no se encontró solución
        return None, nodes_expanded, 0, 0


# Función para generar reporte con la cantidad de nodos expandidos, la profundidad del árbol y el tiempo de cómputo
def generar_reporte(nodes_expanded, depth, computation_time):
    print(f"Nodos expandidos: {nodes_expanded}")
    print(f"Profundidad del árbol: {depth}")
    print(f"Tiempo de cómputo: {computation_time:.2f} segundos")    


