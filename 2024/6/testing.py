import numpy as np
import copy
import matplotlib.pyplot as plt

def save_plot(grid, i, entry):
    plt.imshow(grid)
    plt.colorbar()
    plt.savefig(f"./out/grid_{entry}_{i}.jpg", dpi=800)
    plt.clf()

class Player:
    def __init__(self, board, direction=0):
        self.board = copy.deepcopy(board)
        self.direction = direction  # 0 = up, 1 = right, 2 = down, 3 = left
        self.dimensions = (len(board), len(board[0]))
        self.location = (0, 0)
        self.unique_loc = set()
        self.visits = np.zeros(self.dimensions, dtype=int)
        self.find_location()

    def find_location(self):
        """Find the starting location (^) on the board."""
        for i in range(self.dimensions[0]):
            for j in range(self.dimensions[1]):
                if self.board[i, j] == "^":
                    self.location = (i, j)
                    self.unique_loc.add(self.location)
                    return

    def is_valid_move(self, next_loc):
        """Check if the next location is within bounds and not blocked."""
        x, y = next_loc
        if 0 <= x < self.dimensions[0] and 0 <= y < self.dimensions[1]:
            return self.board[x, y] != "#"
        return False

    def move(self):
        """Move the guard based on the patrol rules."""
        x, y = self.location
        # Directions: 0 = up, 1 = right, 2 = down, 3 = left
        moves = [(-1, 0), (0, 1), (1, 0), (0, -1)]
        next_dir = self.direction % 4
        next_loc = (x + moves[next_dir][0], y + moves[next_dir][1])

        if not (0 <= next_loc[0] < self.dimensions[0] and 0 <= next_loc[1] < self.dimensions[1]):
            # Exit condition: Guard leaves the board
            return False

        if self.is_valid_move(next_loc):
            # Move forward
            self.unique_loc.add(self.location)
            self.visits[x, y] += 1
            self.board[x, y] = "X"
            self.location = next_loc
            self.board[self.location[0], self.location[1]] = "^"
        else:
            # Turn right if blocked
            self.direction = (self.direction + 1) % 4

        return True  # Continue until guard leaves the board
print(1)
# Load and prepare the board
file1 = open("my_file.csv", "r").read()
file1 = np.array([list(x) for x in file1.strip().split("\n")])

# Initial run to determine unique locations
file2 = copy.deepcopy(file1)
player = Player(file2)

try:
    # Simulate the guard's movement
    while player.move():
        pass
except Exception as e:
    print("Error during simulation:", e)
print(2)
count = 0
# Try placing obstacles at unique locations
for num, cords in enumerate(list(player.unique_loc)):
    i, j = cords
    file2 = copy.deepcopy(file1)
    if file2[i, j] != "#":
        file2[i, j] = "#"
    else:
        continue
    if num % 100 == 0:
    	print(num)
    player2 = Player(file2)
    if player2.location == (i, j):
        print("Skipped player start location")
        continue

    try:
        while player2.move():
            if player2.visits[player2.location[0], player2.location[1]] > 20:
                count += 1
                break
    except Exception as e:
        print("Error during obstacle simulation:", e)

print("Total loops created:", count)
