import time

def profundidad_evitando_ciclos(world_data):
    start_time = time.perf_counter()
    
    def expand(node):
        nonlocal nodes_expanded
        nodes_expanded += 1
        x, y, path = node
        for dx, dy in [(0, 1), (0, -1), (1, 0), (-1, 0)]:
            nx, ny = x + dx, y + dy
            if 0 <= nx < 10 and 0 <= ny < 10 and (nx, ny) not in path and world_data[ny][nx] != 1:
                if world_data[ny][nx] == 5:
                    return path + [(nx, ny)]
                else:
                    result = expand((nx, ny, path + [(nx, ny)]))
                    if result:
                        return result
        return None
    
    nodes_expanded = 0
    start_position = None
    for y in range(10):
        for x in range(10):
            if world_data[y][x] == 2:
                start_position = (x, y)
                break
        if start_position:
            break
    
    if start_position:
        path = expand((start_position[0], start_position[1], [start_position]))
        depth = len(path) if path else 0
        end_time = time.perf_counter()
        computation_time = end_time - start_time
        return path, nodes_expanded, depth, computation_time
    else:
        return None, nodes_expanded, 0, 0

def guardar_solucion(world_data, path, output_file):
    if path:
        with open(output_file, "w") as file:
            for y in range(10):
                for x in range(10):
                    if (x, y) in path:
                        file.write("X ")
                    else:
                        file.write(str(world_data[y][x]) + " ")
                file.write("\n")
        print(f"Solución guardada en '{output_file}'.")
    else:
        print("No se encontró solución.")

def generar_reporte(nodes_expanded, depth, computation_time):
    print(f"Nodos expandidos: {nodes_expanded}")
    print(f"Profundidad del árbol: {depth}")
    print(f"Tiempo de cómputo: {computation_time:.2f} segundos")


