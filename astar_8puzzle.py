import heapq

start_state = (8, 1, 3, 4, 0, 2, 7, 6, 5)
goal_state = (1, 2, 3, 4, 5, 6, 7, 8, 0)


def misplaced_tiles(state):
    count = 0
    for position in range(9):
        if state[position] != 0 and state[position] != goal_state[position]:
            count = count + 1
    return count


def manhattan_distance(state):
    total = 0
    for position in range(9):
        tile = state[position]
        if tile == 0:
            continue
        goal_position = goal_state.index(tile)
        row_gap = abs(position // 3 - goal_position // 3)
        column_gap = abs(position % 3 - goal_position % 3)
        total = total + row_gap + column_gap
    return total


def is_solvable(state):
    tiles = [tile for tile in state if tile != 0]
    inversions = 0
    for i in range(len(tiles)):
        for j in range(i + 1, len(tiles)):
            if tiles[i] > tiles[j]:
                inversions = inversions + 1
    return inversions % 2 == 0


def get_neighbours(state):
    neighbours = []
    blank = state.index(0)
    row = blank // 3
    column = blank % 3

    moves = [
        ("Up", -1, 0),
        ("Down", 1, 0),
        ("Left", 0, -1),
        ("Right", 0, 1),
    ]

    for name, row_change, column_change in moves:
        new_row = row + row_change
        new_column = column + column_change

        if 0 <= new_row < 3 and 0 <= new_column < 3:
            new_blank = new_row * 3 + new_column
            new_state = list(state)
            new_state[blank], new_state[new_blank] = new_state[new_blank], new_state[blank]
            neighbours.append((tuple(new_state), name))

    return neighbours


def build_path(came_from, state):
    states = []
    moves = []
    while state is not None:
        parent, move = came_from[state]
        states.append(state)
        moves.append(move)
        state = parent
    states.reverse()
    moves.reverse()
    return states, moves


def a_star(start, heuristic):
    open_list = [(heuristic(start), 0, start)]
    came_from = {start: (None, "Start")}
    best_cost = {start: 0}
    nodes_expanded = 0

    while open_list:
        f_value, g_value, current = heapq.heappop(open_list)

        if g_value > best_cost[current]:
            continue

        if current == goal_state:
            states, moves = build_path(came_from, current)
            return states, moves, nodes_expanded

        nodes_expanded = nodes_expanded + 1

        for neighbour, move in get_neighbours(current):
            new_cost = g_value + 1

            if neighbour not in best_cost or new_cost < best_cost[neighbour]:
                best_cost[neighbour] = new_cost
                came_from[neighbour] = (current, move)
                f_new = new_cost + heuristic(neighbour)
                heapq.heappush(open_list, (f_new, new_cost, neighbour))

    return None, None, nodes_expanded


def print_state(state):
    for row in range(3):
        line = ""
        for column in range(3):
            tile = state[row * 3 + column]
            if tile == 0:
                line = line + "_ "
            else:
                line = line + str(tile) + " "
        print(line)


def main():
    print("Choose heuristic:")
    print("1. Misplaced Tiles")
    print("2. Manhattan Distance")
    choice = input("Enter 1 or 2: ")

    if choice == "1":
        heuristic = misplaced_tiles
    else:
        heuristic = manhattan_distance

    if not is_solvable(start_state):
        print("This puzzle cannot be solved.")
        return

    states, moves, nodes_expanded = a_star(start_state, heuristic)

    if states is None:
        print("No solution found.")
        return

    for step in range(len(states)):
        g_value = step
        h_value = heuristic(states[step])
        f_value = g_value + h_value
        print("Step", step, "- Move:", moves[step])
        print("g =", g_value, " h =", h_value, " f =", f_value)
        print_state(states[step])
        print()

    print("Goal reached in", len(states) - 1, "moves.")
    print("Nodes expanded:", nodes_expanded)


main()
