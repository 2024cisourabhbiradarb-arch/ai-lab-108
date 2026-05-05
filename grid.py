import random

class GridWorld:
    def __init__(self, size=4):
        self.size = size
        self.grid = [["." for _ in range(size)] for _ in range(size)]
        
        # Place agent at start
        self.agent_pos = (0, 0)
        
        # Randomly place Wumpus and Gold
        self.wumpus_pos = (random.randint(0, size-1), random.randint(0, size-1))
        self.gold_pos = (random.randint(0, size-1), random.randint(0, size-1))
        
        # Mark them on the grid
        self.grid[self.wumpus_pos[0]][self.wumpus_pos[1]] = "W"
        self.grid[self.gold_pos[0]][self.gold_pos[1]] = "G"

    def display(self):
        for row in self.grid:
            print(" ".join(row))
        print(f"Agent at {self.agent_pos}")

    def move(self, direction):
        x, y = self.agent_pos
        if direction == "up" and x > 0:
            x -= 1
        elif direction == "down" and x < self.size - 1:
            x += 1
        elif direction == "left" and y > 0:
            y -= 1
        elif direction == "right" and y < self.size - 1:
            y += 1
        else:
            print("Invalid move!")
            return
        self.agent_pos = (x, y)
        self.check_status()

    def check_status(self):
        if self.agent_pos == self.wumpus_pos:
            print("💀 You were eaten by the Wumpus!")
        elif self.agent_pos == self.gold_pos:
            print("🏆 You found the gold!")

    def sense(self):
        x, y = self.agent_pos
        senses = []
        if abs(x - self.wumpus_pos[0]) + abs(y - self.wumpus_pos[1]) == 1:
            senses.append("You smell a Wumpus nearby!")
        if abs(x - self.gold_pos[0]) + abs(y - self.gold_pos[1]) == 1:
            senses.append("You see a glimmer nearby!")
        return senses


# Example usage
world = GridWorld(size=4)
world.display()

world.move("right")
print(world.sense())

world.move("down")
print(world.sense())