maze = [
    [0, 1, 0, 0],
    [0, 1, 0, 1],
    [0, 1, 0, 0],
    [0, 0, 0, 0],
]

start = (0, 0)
goal = (3, 3)

moves = [(1, 0), (-1, 0), (0, 1), (0, -1)]


def is_valid_move(row, column, visited):
    inside_maze = 0 <= row < len(maze) and 0 <= column < len(maze[0])
    if not inside_maze:
        return False
    if maze[row][column] == 1:
        return False
    if (row, column) in visited:
        return False
    return True


def dfs(row, column, visited, path):
    visited.add((row, column))
    path.append((row, column))

    if (row, column) == goal:
        return True

    for row_change, column_change in moves:
        next_row = row + row_change
        next_column = column + column_change

        if is_valid_move(next_row, next_column, visited):
            if dfs(next_row, next_column, visited, path):
                return True

    path.pop()
    return False


def show_maze(path):
    for row in range(len(maze)):
        line = ""
        for column in range(len(maze[0])):
            if (row, column) == start:
                line = line + "S "
            elif (row, column) == goal:
                line = line + "G "
            elif (row, column) in path:
                line = line + "* "
            elif maze[row][column] == 1:
                line = line + "# "
            else:
                line = line + ". "
        print(line)


def main():
    visited = set()
    path = []

    if dfs(start[0], start[1], visited, path):
        print("Path found:")
        print(path)
        print("Number of steps:", len(path) - 1)
        print()
        show_maze(path)
    else:
        print("No path exists from start to goal.")


main()
