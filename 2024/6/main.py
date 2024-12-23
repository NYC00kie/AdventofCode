import numpy as np
import copy
import matplotlib.pyplot as plt
#part 2
# 1743 too high
# 1700 too high
# 1791 is wrong
# 1602 is right (not from my code)

# Yes, im basicly making a game.

def save_plot(grid,i,entry):
    plt.imshow(grid)
    plt.colorbar()
    plt.savefig(f"./out/grid_{entry}_{i}.jpg", dpi=800)
    plt.clf()

class Player(object):
	"""docstring for Player"""
	def __init__(self, board, direction=0):
		super(Player, self).__init__()
		self.board = board
		self.direction = direction
		self.dimensions = (len(board),len(board[0]))
		self.location = (0,0)
		self.unique_loc = set([])
		self.locations = []
		self.visits = np.zeros([len(self.board),len(self.board[0])])
		self.find_location()

	def __str__(self):
		return str((self.board,self.unique_loc))

	def find_location(self):
		for i in range(len(self.board)):
			for j in range(len(self.board[i])):
				if self.board[i,j] == "^":
					self.location = (i,j)
					self.unique_loc = set([(i,j)])
					return None;

	def move(self):
		# directions are 0 up, 1 right, 2 down, 3 left
		
		if self.location < self.dimensions:
			# up
			if self.direction % 4 == 0 and self.board[self.location[0]-1,self.location[1]] != "#":
				self.unique_loc.add(self.location)
				self.visits[self.location[0],self.location[1]] += 1
				self.locations.append(self.location)
				self.board[self.location[0],self.location[1]] = "X"
				self.location = (self.location[0]-1,self.location[1])
				self.board[self.location[0],self.location[1]] = "^"
				return True;
			elif self.direction % 4 == 0 and self.board[self.location[0]-1,self.location[1]] == "#":
				self.direction -= 1
				return True;
			#right
			if self.direction % 4 == 1 and self.board[self.location[0],self.location[1]-1] != "#":
				self.unique_loc.add(self.location)
				self.visits[self.location[0],self.location[1]] += 1
				self.locations.append(self.location)
				self.board[self.location[0],self.location[1]] = "X"
				self.location = (self.location[0],self.location[1]-1)
				self.board[self.location[0],self.location[1]] = "^"
				return True;
			elif self.direction % 4 == 1 and self.board[self.location[0],self.location[1]-1] == "#":
				self.direction -= 1
				return True;
			#down
			if self.direction % 4 == 2 and self.board[self.location[0]+1,self.location[1]] != "#":
				self.unique_loc.add(self.location)
				self.visits[self.location[0],self.location[1]] += 1
				self.locations.append(self.location)
				self.board[self.location[0],self.location[1]] = "X"
				self.location = (self.location[0]+1,self.location[1])
				self.board[self.location[0],self.location[1]] = "^"
				return True;
			elif self.direction % 4 == 2 and self.board[self.location[0]+1,self.location[1]] == "#":
				self.direction -= 1
				return True;

			#left
			if self.direction % 4 == 3 and self.board[self.location[0],self.location[1]+1] != "#":
				self.unique_loc.add(self.location)
				self.visits[self.location[0],self.location[1]] += 1
				self.locations.append(self.location)
				self.board[self.location[0],self.location[1]] = "X"
				self.location = (self.location[0],self.location[1]+1)
				self.board[self.location[0],self.location[1]] = "^"
				return True;
			elif self.direction % 4 == 3 and self.board[self.location[0],self.location[1]+1] == "#":
				self.direction -= 1
				return True;
		else:
			return False



# first pass to see what spots actually influence the path
file1 = open("my_file.csv", "r").read()
file1 = np.array([list(x) for x in file1.split("\n")])

file2 = copy.deepcopy(file1)
player = Player(file2)
try:
	while player.move():
		pass
		#print(player)

except Exception as e:
	player.unique_loc.add(player.location)
	print(player.direction)
	print(e)


count = 0
#going over the just gotten spots and see if it loops or not by simulating it like in part 1.
for num,cords in enumerate(list(player.unique_loc)):
	i,j = cords
	file2 = copy.deepcopy(file1)
	if file2[i,j] != "#":
		file2[i,j] = "#"
	else:
		continue
	if num % 100 == 0:
		print(len(player.unique_loc),num,i,j)
	player2 = Player(file2)
	if player2.location == (i,j):
		print("skipped Player location")
		continue

	try:
		c = 0
		while player2.move():
			c += 1
			# if c % 1000 == 0:
				# save_plot(player2.visits,c,num)
				# print(len(player.unique_loc),num,i,j, player2.visits[player2.location[0],player2.location[1]], c, sum(sum(player2.visits)),len(file2)*len(file2[0]), len(list(player2.unique_loc)))
			
			# this is the loop condition.
			if player2.visits[player2.location[0],player2.location[1]] > 20:
				count += 1
				break;
			#print(player)

		
	except IndexError as e:
		# print(e)
		pass


print(count)