from collections import deque

grid = [
    [0, 0, 0, 0, 0],
    [0, 1, 1, 1, 0],
    [0, 0, 0, 1, 0],
    [1, 1, 0, 1, 0],
    [0, 0, 0, 0, 0],
]

start = (0, 0)
goal = (4, 4)

moves = {
    "Down": (1, 0),
    "Up": (-1, 0),
    "Right": (0, 1),
    "Left": (0, -1),
}


class Environment:
    def __init__(self, grid):
        self.grid = grid
        self.rows = len(grid)
        self.columns = len(grid[0])

    def perceive(self, position):
        percept = {}
        row, column = position
        percept[position] = self.grid[row][column]

        for row_change, column_change in moves.values():
            neighbour_row = row + row_change
            neighbour_column = column + column_change
            inside_grid = 0 <= neighbour_row < self.rows and 0 <= neighbour_column < self.columns
            if inside_grid:
                percept[(neighbour_row, neighbour_column)] = self.grid[neighbour_row][neighbour_column]

        return percept


class ModelBasedAgent:
    def __init__(self, start, goal, rows, columns):
        self.position = start
        self.goal = goal
        self.rows = rows
        self.columns = columns
        self.known_cells = {}
        self.path_taken = [start]

    def update_state(self, percept):
        self.known_cells.update(percept)

    def is_blocked(self, cell):
        return self.known_cells.get(cell) == 1

    def plan_path(self):
        queue = deque([self.position])
        came_from = {self.position: None}

        while queue:
            current = queue.popleft()

            if current == self.goal:
                path = []
                while current is not None:
                    path.append(current)
                    current = came_from[current]
                path.reverse()
                return path

            for row_change, column_change in moves.values():
                next_row = current[0] + row_change
                next_column = current[1] + column_change
                next_cell = (next_row, next_column)

                inside_grid = 0 <= next_row < self.rows and 0 <= next_column < self.columns
                if inside_grid and not self.is_blocked(next_cell) and next_cell not in came_from:
                    came_from[next_cell] = current
                    queue.append(next_cell)

        return None

    def choose_next_cell(self):
        path = self.plan_path()
        if path is None or len(path) < 2:
            return None
        return path[1]

    def move_to(self, cell):
        self.position = cell
        self.path_taken.append(cell)


def get_action_name(current, next_cell):
    change = (next_cell[0] - current[0], next_cell[1] - current[1])
    for name, move in moves.items():
        if move == change:
            return name


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
    environment = Environment(grid)
    agent = ModelBasedAgent(start, goal, environment.rows, environment.columns)
    step = 0

    while agent.position != goal:
        percept = environment.perceive(agent.position)
        agent.update_state(percept)

        next_cell = agent.choose_next_cell()
        if next_cell is None:
            print("Agent cannot reach the goal.")
            return

        action = get_action_name(agent.position, next_cell)
        step = step + 1
        print("Step", step, "- Action:", action, "->", next_cell)
        agent.move_to(next_cell)

    print()
    print("Goal reached in", step, "steps.")
    print("Path taken:", agent.path_taken)
    print("Cells known to the agent:", len(agent.known_cells))
    print()
    show_grid(agent.path_taken)


main()
