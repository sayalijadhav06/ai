from collections import deque

class tower_of_hanoi:
    def __init__(self, num_disk):
        self.num_disk = num_disk
        self.start_state = tuple([0] * num_disk)
        self.goal_state = tuple([2] * num_disk)

    def get_top_disk(self, state):
        top = [None, None, None]

        for disk in range(self.num_disk):
            rod = state[disk]
            if top[rod] is None:
                top[rod] = disk

        return top

    def get_successor(self, state):
        successor = []
        top = self.get_top_disk(state)

        for src in range(3):
            if top[src] is None:
                continue

            for dst in range(3):
                if src == dst:
                    continue

                if top[dst] is None or top[src] < top[dst]:
                    new_state = list(state)
                    disk = top[src]
                    new_state[disk] = dst

                    move = ("Move disk " + str(disk + 1) +
                            " from " + chr(65 + src) +
                            " to " + chr(65 + dst))

                    successor.append((tuple(new_state), move))

        return successor

    def bfs_search(self):
        queue = deque([self.start_state])
        parent = {self.start_state: None}
        move_taken = {self.start_state: None}
        node_explore = 0

        while queue:
            state = queue.popleft()
            node_explore += 1

            if state == self.goal_state:
                path = []
                current = state

                while current is not None:
                    path.append((current, move_taken[current]))
                    current = parent[current]

                path.reverse()
                return path, node_explore

            for next_state, move in self.get_successor(state):
                if next_state not in parent:
                    parent[next_state] = state
                    move_taken[next_state] = move
                    queue.append(next_state)

        return None, node_explore


def display_state(state, num_disk):
    rods = {0: [], 1: [], 2: []}

    for disk in range(num_disk - 1, -1, -1):
        rods[state[disk]].append(disk + 1)

    return f"A={rods[0]} B={rods[1]} C={rods[2]}"


def main():
    num_disk = int(input("Enter number of disks: "))
    solver = tower_of_hanoi(num_disk)

    print("Start:", display_state(solver.start_state, num_disk))
    print("Goal:", display_state(solver.goal_state, num_disk))

    path, node_explore = solver.bfs_search()

    if path is None:
        print("No solution found")
        return

    print("States explored:", node_explore)
    print("Minimum moves:", len(path) - 1)

    for step, (state, move) in enumerate(path):
        if step == 0:
            print("Initial state")
        else:
            print("Step", step, ":", move)

        print(display_state(state, num_disk))


if __name__ == "__main__":
    main()
