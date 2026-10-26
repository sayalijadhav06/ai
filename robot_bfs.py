from collections import deque

grid = [
    [0, 0, 0, 1, 0],
    [1, 1, 0, 1, 0],
    [0, 0, 0, 0, 0],
    [0, 1, 1, 1, 0],
    [0, 0, 0, 0, 0],
]

start = (0, 0)
goal = (4, 4)

moves = [(1, 0), (-1, 0), (0, 1), (0, -1)]


def is_valid_move(row, column, visited):
    inside_grid = 0 <= row < len(grid) and 0 <= column < len(grid[0])
    if not inside_grid:
        return False
    if grid[row][column] == 1:
        return False
    if (row, column) in visited:
        return False
    return True


def build_path(came_from, goal_cell):
    path = []
    cell = goal_cell
    while cell is not None:
        path.append(cell)
        cell = came_from[cell]
    path.reverse()
    return path


def bfs(start_cell, goal_cell):
    queue = deque([start_cell])
    visited = {start_cell}
    came_from = {start_cell: None}

    while queue:
        current = queue.popleft()

        if current == goal_cell:
            return build_path(came_from, goal_cell)

        for row_change, column_change in moves:
            next_row = current[0] + row_change
            next_column = current[1] + column_change

            if is_valid_move(next_row, next_column, visited):
                next_cell = (next_row, next_column)
                visited.add(next_cell)
                came_from[next_cell] = current
                queue.append(next_cell)

    return None


def show_grid(path):
    for row in range(len(grid)):
        line = ""
        for column in range(len(grid[0])):
            if (row, column) == start:
                line = line + "S "
            elif (row, column) == goal:
                line = line + "G "
            elif (row, column) in path:
                line = line + "* "
            elif grid[row][column] == 1:
                line = line + "# "
            else:
                line = line + ". "
        print(line)


def main():
    path = bfs(start, goal)

    if path is None:
        print("No path exists from start to goal.")
        return

    print("Shortest path found:")
    print(path)
    print("Number of steps:", len(path) - 1)
    print()
    show_grid(path)


main()
