class VacuumEnvironment:
    def __init__(self, room_a, room_b, location):
        self.rooms = {"A": room_a, "B": room_b}
        self.location = location

    def perceive(self):
        return self.location, self.rooms[self.location]

    def execute(self, action):
        if action == "Suck":
            self.rooms[self.location] = "Clean"
        elif action == "Right":
            self.location = "B"
        elif action == "Left":
            self.location = "A"

    def count_clean_rooms(self):
        count = 0
        for status in self.rooms.values():
            if status == "Clean":
                count = count + 1
        return count


def simple_reflex_agent(percept):
    location, status = percept

    if status == "Dirty":
        return "Suck"
    if location == "A":
        return "Right"
    return "Left"


def run_simulation(room_a, room_b, location, steps, show_steps):
    environment = VacuumEnvironment(room_a, room_b, location)
    score = 0

    for step in range(1, steps + 1):
        percept = environment.perceive()
        action = simple_reflex_agent(percept)
        environment.execute(action)
        score = score + environment.count_clean_rooms()

        if show_steps:
            print("Step", step)
            print("  Percept :", percept)
            print("  Action  :", action)
            print("  Rooms   :", environment.rooms, "| Agent in", environment.location)
            print("  Score   :", score)

    return score


def main():
    steps = 6

    print("Detailed run: A = Dirty, B = Dirty, agent starts in A")
    print()
    run_simulation("Dirty", "Dirty", "A", steps, True)

    print()
    print("All possible starting situations (", steps, "steps each )")
    print()
    print("Room A   Room B   Start   Score")

    for room_a in ["Clean", "Dirty"]:
        for room_b in ["Clean", "Dirty"]:
            for location in ["A", "B"]:
                score = run_simulation(room_a, room_b, location, steps, False)
                print(room_a.ljust(8), room_b.ljust(8), location.ljust(7), score)


main()
