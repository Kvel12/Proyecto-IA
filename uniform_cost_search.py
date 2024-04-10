import heapq
import time

def uniform_cost_search(env):
    start = env.start
    goal = env.goal
    frontier = []
    heapq.heappush(frontier, (0, start))
    came_from = {}
    cost_so_far = {}
    came_from[start] = None
    cost_so_far[start] = 0
    visited_in_ship = set()  
    nodes_expanded = 0  # Contador de nodos expandidos
    max_depth = 0  # Profundidad máxima del árbol
    start_time = time.time()  # Tiempo de inicio de la búsqueda

    while frontier:
        current_cost, current_pos = heapq.heappop(frontier)
        max_depth = max(max_depth, len(came_from))  # Actualizar profundidad máxima
        if current_pos == goal:
            break
        
        nodes_expanded += 1  # Incrementar contador de nodos expandidos

        for next_pos in env.get_neighbors(current_pos):
            new_cost = current_cost + get_move_cost(env, current_pos, next_pos, visited_in_ship)
            if next_pos not in cost_so_far or new_cost < cost_so_far[next_pos]:
                cost_so_far[next_pos] = new_cost
                priority = new_cost
                heapq.heappush(frontier, (priority, next_pos))
                came_from[next_pos] = current_pos
    
    end_time = time.time()  # Tiempo de finalización de la búsqueda
    computation_time = end_time - start_time  # Tiempo de cómputo

    path = reconstruct_path(came_from, start, goal)
    cost = cost_so_far[goal]

    return path, cost, nodes_expanded, max_depth, computation_time

# Resto de tu código aquí ...


def get_move_cost(env, current_pos, next_pos, visited_in_ship=None, entered_ship=False, ship_cells_passed=0):
    if visited_in_ship is None:
        visited_in_ship = set()

    cell_type = env.grid[next_pos[0]][next_pos[1]]
    
    # Verificar si la celda es una nave
    if cell_type == 3:
        # Si la posición actual no está en la nave y no hemos entrado en la nave aún, limpiar el conjunto de visitados
        if current_pos not in visited_in_ship and not entered_ship:
            visited_in_ship.clear()
        visited_in_ship.add(next_pos)  # Agregar la nueva posición de la nave a los visitados
        if not entered_ship:  # Si es la primera vez que entramos en la nave, marcarlo como tal y reiniciar el contador de casillas pasadas
            entered_ship = True
            ship_cells_passed = 0
        return 0.5  # Costo reducido al moverse en la nave
    
    # Si estamos dentro de la nave
    if current_pos in visited_in_ship:
        # Agregar la nueva posición a los visitados
        visited_in_ship.add(next_pos)
        # Incrementar el contador de casillas pasadas dentro de la nave
        ship_cells_passed += 1
        # Verificar si hemos pasado las siguientes 10 casillas después de entrar en la nave
        if ship_cells_passed <= 10:
            return 0.5  # Costo reducido por cada una de las siguientes 10 casillas

    # Resto de las condiciones de movimiento
    if cell_type == 4 and current_pos in visited_in_ship:  # Enemigo y estamos dentro de la nave
        return 0.5  # Costo reducido por pasar por un enemigo dentro de la nave
    
    if cell_type == 4:  # Enemigo fuera de la nave
        return 5  # Costo alto por moverse a través de un enemigo

    return 1  # Movimiento normal si no hay cambios en el costo


def reconstruct_path(came_from, start, goal):
    current = goal
    path = []
    while current != start:
        path.append(current)
        current = came_from[current]
    path.append(start)
    path.reverse()
    return path
