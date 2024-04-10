import heapq
import time

class Node:
    def __init__(self, x, y, parent, cost, h):
        self.x = x
        self.y = y
        self.parent = parent
        self.cost = cost
        self.h = h

    def __lt__(self, other):
        # Comparar los nodos en función de su costo total estimado (costo actual + heurística)
        return self.cost + self.h < other.cost + other.h

def manhattan_distance(x1, y1, x2, y2):
    # Calcular la distancia de Manhattan entre dos puntos
    return abs(x1 - x2) + abs(y1 - y2)

def is_valid_move(world_data, x, y):
    # Verificar si un movimiento es válido en el laberinto
    return 0 <= x < 10 and 0 <= y < 10 and world_data[y][x] != 1

def avara(world_data):
    # Encontrar las coordenadas de inicio y destino
    start_x, start_y = None, None
    target_x, target_y = None, None
    for y in range(len(world_data)):
        for x in range(len(world_data[0])):
            if world_data[y][x] == 2:
                start_x, start_y = x, y
            elif world_data[y][x] == 5:
                target_x, target_y = x, y

    # Cola de prioridad para expandir los nodos
    pq = [(manhattan_distance(start_x, start_y, target_x, target_y), Node(start_x, start_y, None, 0, manhattan_distance(start_x, start_y, target_x, target_y)))]

    # Diccionario para mantener los nodos visitados
    visited = set()

    start_time = time.perf_counter()
    nodes_expanded = 0
    max_depth = 0

    while pq:
        _, current_node = heapq.heappop(pq)
        nodes_expanded += 1

        if current_node.x == target_x and current_node.y == target_y:
            # Llegó a Grogu
            path = []
            while current_node.parent:
                path.append((current_node.y, current_node.x))  # Invertir el orden de las coordenadas
                current_node = current_node.parent
            path.append((start_y, start_x))  # Invertir el orden de las coordenadas del inicio
            path.reverse()
            end_time = time.perf_counter()
            return path, nodes_expanded, len(path) - 1, end_time - start_time  # Devolver la profundidad sin contar la raíz

        if (current_node.x, current_node.y) in visited:
            continue
        visited.add((current_node.x, current_node.y))
        max_depth = max(max_depth, len(visited))

        # Generar los nodos hijos
        neighbors = [(0, 1), (0, -1), (1, 0), (-1, 0)]
        new_nodes = []
        for dx, dy in neighbors:
            new_x, new_y = current_node.x + dx, current_node.y + dy
            if is_valid_move(world_data, new_x, new_y):
                new_h = manhattan_distance(new_x, new_y, target_x, target_y)
                new_node = Node(new_x, new_y, current_node, current_node.cost + 1, new_h)
                new_nodes.append(new_node)

        # Expandir todos los nodos con el mismo costo estimado más bajo
        min_h = min(node.h for node in new_nodes)
        for node in new_nodes:
            if node.h == min_h:
                heapq.heappush(pq, (node.cost + node.h, node))

    # No se encontró solución
    end_time = time.perf_counter()
    return None, nodes_expanded, max_depth, end_time - start_time