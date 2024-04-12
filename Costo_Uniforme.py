import heapq
import time

def costo_uniforme(world_data):
    """
    Aplica el algoritmo de costo uniforme para encontrar el camino más corto desde el punto de inicio hasta el objetivo.

    Args:
        world_data: Los datos del mundo, que incluyen la cuadrícula y la ubicación de inicio y objetivo.

    Returns:
        Una tupla que contiene el camino más corto, el costo del camino, el número de nodos expandidos, la profundidad máxima alcanzada y el tiempo de computación.
    """
    start = find_start(world_data)
    goal = find_goal(world_data)
    frontier = []
    heapq.heappush(frontier, (0, start))
    came_from = {}
    cost_so_far = {}
    came_from[start] = None
    cost_so_far[start] = 0
    visited_in_ship = set()
    nodes_expanded = 0
    depth = 0
    start_time = time.time()

    while frontier:
        current_cost, current_pos = heapq.heappop(frontier)
        depth = max(depth, len(came_from))

        if current_pos == goal:
            break

        nodes_expanded += 1

        for next_pos in get_neighbors(world_data, current_pos):
            new_cost = current_cost + get_move_cost(world_data, current_pos, next_pos, visited_in_ship)
            if next_pos not in cost_so_far or new_cost < cost_so_far[next_pos]:
                cost_so_far[next_pos] = new_cost
                priority = new_cost
                heapq.heappush(frontier, (priority, next_pos))
                came_from[next_pos] = current_pos

    end_time = time.time()
    computation_time = end_time - start_time
    path = reconstruct_path(came_from, start, goal)
    cost = cost_so_far[goal]
    return path, cost, nodes_expanded, depth, computation_time

def get_neighbors(grid, current_pos):
    """
    Encuentra los vecinos válidos de una posición dada en la cuadrícula.

    Args:
        grid: La cuadrícula que representa el mundo.
        current_pos: La posición actual en la cuadrícula.

    Returns:
        Una lista de posiciones vecinas válidas.
    """
    x, y = current_pos
    neighbors = [(x+1, y), (x-1, y), (x, y+1), (x, y-1)]
    valid_neighbors = [(nx, ny) for nx, ny in neighbors if is_valid_move(grid, (nx, ny))]
    return valid_neighbors

def is_valid_move(grid, position):
    """
    Verifica si una posición dada en la cuadrícula es válida para moverse.

    Args:
        grid: La cuadrícula que representa el mundo.
        position: La posición en la cuadrícula que se está verificando.

    Returns:
        True si la posición es válida para moverse, False en caso contrario.
    """
    x, y = position
    if 0 <= x < len(grid) and 0 <= y < len(grid[0]) and grid[x][y] != 1:
        return True
    return False

def find_start(grid):
    """
    Encuentra la posición de inicio en la cuadrícula.

    Args:
        grid: La cuadrícula que representa el mundo.

    Returns:
        La posición de inicio en la cuadrícula.
    """
    for i in range(len(grid)):
        for j in range(len(grid[0])):
            if grid[i][j] == 2:
                return (i, j)

def find_goal(grid):
    """
    Encuentra la posición objetivo en la cuadrícula.

    Args:
        grid: La cuadrícula que representa el mundo.

    Returns:
        La posición objetivo en la cuadrícula.
    """
    for i in range(len(grid)):
        for j in range(len(grid[0])):
            if grid[i][j] == 5:
                return (i, j)


def get_move_cost(grid, current_pos, next_pos, visited_in_ship=None, entered_ship=False, ship_cells_passed=0):
    """
    Calcula el costo de moverse desde una posición actual a una posición vecina en la cuadrícula.

    Args:
        grid: La cuadrícula que representa el mundo.
        current_pos: La posición actual.
        next_pos: La siguiente posición a la que se quiere mover.
        visited_in_ship: Un conjunto de posiciones visitadas en una nave.
        entered_ship: Un indicador de si se ha entrado en una nave.
        ship_cells_passed: El número de celdas de nave pasadas.

    Returns:
        El costo de moverse desde la posición actual a la siguiente posición.
    """
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
            return 0.5  # Costo reducido por cada una de las siguientes 10 casillas dentro de la nave
        else:
            return 1  # Costo normal después de las primeras 10 casillas dentro de la nave

    if cell_type == 4 and current_pos in visited_in_ship:
        return 0.5  # Costo reducido por pasar por un enemigo dentro de la nave
    if cell_type == 4:
        return 5  # Costo alto por moverse a través de un enemigo

    return 1  # Movimiento normal si no hay cambios en el costo


def reconstruct_path(came_from, start, goal):
    """
    Reconstruye el camino más corto desde el punto de inicio hasta el objetivo.

    Args:
        came_from: Un diccionario que contiene los nodos visitados y sus predecesores.
        start: La posición de inicio.
        goal: La posición objetivo.

    Returns:
        El camino más corto desde el punto de inicio hasta el objetivo.
    """
    current = goal
    path = []
    while current != start:
        path.append(current)
        current = came_from[current]
    path.append(start)
    path.reverse()
    return path

def g(path, grid):
    """
    Calcula el costo total del camino.

    Args:
        path: El camino desde el punto de inicio hasta el objetivo.
        grid: La cuadrícula que representa el mundo.

    Returns:
        El costo total del camino.
    """
    costo_total = 0
    en_nave = False
    combustible_nave = 10
    for i in range(len(path) - 1):
        
        next_pos = path[i + 1]
        if grid[next_pos[0]][next_pos[1]] == 3:  # Si es la nave
            en_nave = True
            combustible_nave = 10  # Reiniciar el combustible de la nave
        if en_nave:
            costo = 0.5  # Costo reducido dentro de la nave
            combustible_nave -= 1
            if combustible_nave <= 0:  # Si se agota el combustible, volver al costo normal
                en_nave = False
        elif grid[next_pos[0]][next_pos[1]] == 4:  # Si hay un enemigo
            costo = 5  # Costo alto por pasar por un enemigo
        else:
            costo = 1  # Costo normal de movimiento
        costo_total += costo
    return costo_total



