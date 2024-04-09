import heapq
import time

class Node:
    def __init__(self, x, y, parent, cost, heuristic):
        self.x = x
        self.y = y
        self.parent = parent
        self.cost = cost
        self.heuristic = heuristic

    def __lt__(self, other):
        # Primero compara el costo, luego el valor heurístico
        if self.cost != other.cost:
            return self.cost < other.cost
        else:
            return self.heuristic < other.heuristic

def manhattan_distance(x1, y1, x2, y2):
    return abs(x1 - x2) + abs(y1 - y2)

def is_valid_move(world_data, x, y):
    return 0 <= x < 10 and 0 <= y < 10 and world_data[y][x] != 1  # Verificar si no es un muro

def avara(world_data):
    start_x, start_y = 3, 0  # Coordenadas de inicio
    target_x, target_y = 0, 9  # Coordenadas de Grogu

    # Cola de prioridad para expandir los nodos
    pq = [(12, Node(start_x, start_y, None, 0, 12))]

    # Diccionario para mantener los nodos visitados
    visited = set()

    start_time = time.perf_counter()
    nodes_expanded = 0
    max_depth = 0

    while pq:
        _, current_node = heapq.heappop(pq)
        nodes_expanded += 1

        if current_node.x == target_x and current_node.y == target_y:  # Llegó a Grogu
            path = []
            while current_node.parent:
                path.append((current_node.x, current_node.y))
                current_node = current_node.parent
            path.append((start_x, start_y))
            path.reverse()
            end_time = time.perf_counter()
            return path, nodes_expanded, len(path), end_time - start_time

        if (current_node.x, current_node.y) in visited:
            continue
        visited.add((current_node.x, current_node.y))

        max_depth = max(max_depth, len(visited))

        # Generar los nodos hijos
        for dx, dy in [(0, 1), (0, -1), (1, 0), (-1, 0)]:
            new_x, new_y = current_node.x + dx, current_node.y + dy

            if is_valid_move(world_data, new_x, new_y):
                new_heuristic = manhattan_distance(new_x, new_y, target_x, target_y)
                new_node = Node(new_x, new_y, current_node, current_node.cost + 1, new_heuristic)
                heapq.heappush(pq, (new_node.cost, new_node))

    # No se encontró solución
    return None, nodes_expanded, max_depth, time.perf_counter() - start_time