import time
def load_world(file_path):
    with open(file_path, 'r') as file:
        grid = [[int(num) for num in line.split()] for line in file]
    return grid

def find_start(grid):
    for i in range(len(grid)):
        for j in range(len(grid[0])):
            if grid[i][j] == 2:
                return (i, j)

def find_goal(grid):
    for i in range(len(grid)):
        for j in range(len(grid[0])):
            if grid[i][j] == 5:
                return (i, j)

def is_valid_move(grid, position):
    x, y = position
    if 0 <= x < len(grid) and 0 <= y < len(grid[0]) and grid[x][y] != 1:
        return True
    return False

def get_neighbors(grid, position):
    x, y = position
    neighbors = [(x+1, y), (x-1, y), (x, y+1), (x, y-1)]
    valid_neighbors = [(nx, ny) for nx, ny in neighbors if is_valid_move(grid, (nx, ny))]
    return valid_neighbors

def busqueda_amplitud(world_data):
    start = find_start(world_data)
    goal = find_goal(world_data)
    frontier = [start]
    came_from = {}
    visited = set()
    nodes_expanded = 0
    max_depth = 0
    start_time = time.time()

    while frontier:
        current_pos = frontier.pop(0)
        max_depth = max(max_depth, len(came_from))

        if current_pos == goal:
            break

        nodes_expanded += 1
        visited.add(current_pos)

        for next_pos in get_neighbors(world_data, current_pos):
            if next_pos not in visited and next_pos not in frontier:
                frontier.append(next_pos)
                came_from[next_pos] = current_pos

    end_time = time.time()
    computation_time = end_time - start_time

    path = reconstruct_path(came_from, start, goal)
    cost = len(path) - 1

    return path, cost, nodes_expanded, max_depth, computation_time

def reconstruct_path(came_from, start, goal):
    current = goal
    path = []
    while current != start:
        path.append(current)
        current = came_from[current]
    path.append(start)
    path.reverse()
    return path



