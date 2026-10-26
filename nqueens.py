def create_board(size):
    return [[0] * size for _ in range(size)]


def print_board(board):
    for row in board:
        line = ""
        for cell in row:
            if cell == 1:
                line = line + "Q "
            else:
                line = line + ". "
        print(line)
    print()


def is_safe(board, row, column):
    size = len(board)

    for left_column in range(column):
        if board[row][left_column] == 1:
            return False

    r = row
    c = column
    while r >= 0 and c >= 0:
        if board[r][c] == 1:
            return False
        r = r - 1
        c = c - 1

    r = row
    c = column
    while r < size and c >= 0:
        if board[r][c] == 1:
            return False
        r = r + 1
        c = c - 1

    return True


def solve(board, column):
    size = len(board)

    if column == size:
        return True

    for row in range(size):
        if is_safe(board, row, column):
            board[row][column] = 1

            if solve(board, column + 1):
                return True

            board[row][column] = 0

    return False


def main():
    size = int(input("Enter the number of queens (8 for 8-Queens): "))
    board = create_board(size)

    if solve(board, 0):
        print("Solution found:\n")
        print_board(board)
    else:
        print("No solution exists for " + str(size) + " queens.")


main()
