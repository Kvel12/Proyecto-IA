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

def a_star(world_data):
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
            if current_node.h == 0:  # Verificar que la distancia de Manhattan sea cero
                path = []
                final_cost = current_node.cost
                while current_node.parent:
                    path.append((current_node.y, current_node.x))  # Invertir el orden de las coordenadas
                    current_node = current_node.parent
                path.append((start_y, start_x))  # Invertir el orden de las coordenadas del inicio
                path.reverse()
                end_time = time.perf_counter()
                return path, final_cost, nodes_expanded, len(path) - 1, end_time - start_time

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
                new_cost = current_node.cost + get_move_cost(world_data, (current_node.x, current_node.y), (new_x, new_y))
                new_node = Node(new_x, new_y, current_node, new_cost, new_h)
                new_nodes.append(new_node)

        # Expandir todos los nodos con el mismo costo estimado más bajo
        min_h = min(node.h for node in new_nodes)
        for node in new_nodes:
            if node.h == min_h:
                heapq.heappush(pq, (node.cost + node.h, node))

    # No se encontró solución
    end_time = time.perf_counter()
    return None, None, nodes_expanded, max_depth, end_time - start_time

def get_move_cost(grid, current_pos, next_pos, visited_in_ship=None, entered_ship=False, ship_cells_passed=0):
    if visited_in_ship is None:
        visited_in_ship = set()
    cell_type = grid[next_pos[0]][next_pos[1]]
    
    if cell_type == 3:  # Si la posición es una nave
        if current_pos not in visited_in_ship and not entered_ship:
            visited_in_ship.clear()
            visited_in_ship.add(next_pos)
        if not entered_ship:
            entered_ship = True
            ship_cells_passed = 0
        return 0.5  # Costo reducido al moverse en la nave

    if current_pos in visited_in_ship:
        visited_in_ship.add(next_pos)
        ship_cells_passed += 1
        if ship_cells_passed <= 10:
            return 0.5  # Costo reducido por cada una de las siguientes 10 casillas

    if cell_type == 4 and current_pos in visited_in_ship:
        return 0.5  # Costo reducido por pasar por un enemigo dentro de la nave
    if cell_type == 4:
        return 5  # Costo alto por moverse a través de un enemigo

    return 1  # Movimiento normal si no hay cambios en el costo 