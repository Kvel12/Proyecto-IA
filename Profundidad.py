import time

def profundidad(world_data, max_depth):
    start_time = time.perf_counter()

    explored = set()
    stack = [(0, world_data)]
    nodes_expanded = 0

    while stack:
        depth, current_state = stack.pop()
        nodes_expanded += 1

        if depth > max_depth:
            continue

        if is_goal_state(current_state):
            end_time = time.perf_counter()
            computation_time = end_time - start_time
            return reconstruct_path(current_state), nodes_expanded, depth, computation_time

        explored.add(hash(str(current_state)))

        for action in get_possible_actions(current_state):
            next_state = apply_action(current_state, action)
            if hash(str(next_state)) not in explored:
                stack.append((depth + 1, next_state))

    end_time = time.perf_counter()
    computation_time = end_time - start_time
    return None, nodes_expanded, max_depth, computation_time

def is_goal_state(state):
    for row in state:
        if 5 in row:
            return True
    return False

def get_possible_actions(state):
    actions = []
    for y in range(len(state)):
        for x in range(len(state[y])):
            if state[y][x] != 1:
                actions.append((x, y))
    return actions

def apply_action(state, action):
    x, y = action
    new_state = [row[:] for row in state]
    new_state[y][x] = 2
    return new_state

def reconstruct_path(final_state):
    path = []
    for y in range(len(final_state)):
        for x in range(len(final_state[y])):
            if final_state[y][x] == 2:
                path.append((x, y))
    return path[::-1]  # Invertir el camino para que esté en orden de inicio a fin