import numpy as np
import copy
#part 2
# 1743 too high
# 1700 too high

# Yes, im basicly making a game.

class Player(object):
	"""docstring for Player"""
	def __init__(self, board, direction=0):
		super(Player, self).__init__()
		self.board = board
		self.direction = direction
		self.dimensions = (len(board),len(board[0]))
		self.location = (0,0)
		self.unique_loc = set([])
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
				self.board[self.location[0],self.location[1]] = "X"
				self.location = (self.location[0],self.location[1]+1)
				self.board[self.location[0],self.location[1]] = "^"
				return True;
			elif self.direction % 4 == 3 and self.board[self.location[0],self.location[1]+1] == "#":
				self.direction -= 1
				return True;
		else:
			return False




file1 = open("my_file.csv", "r").read()
count = 0
file1 = np.array([list(x) for x in file1.split("\n")])

file2 = copy.deepcopy(file1)
player = Player(file2)
try:
	while player.move():
		pass
		#print(player)

except Exception as e:
	print(player.direction)
	print(player.board)
	print(len(player.unique_loc)+1)
	print(e)



for cords in list(player.unique_loc):
	if player.location == cords:
		continue
	i,j = cords
	file2 = copy.deepcopy(file1)
	print(i,j)
	if file2[i,j] != "#":
		file2[i,j] = "#"
	else:
		continue

	player = Player(file2)

	try:
		while player.move():
			if player.direction < -10000:
				break;
			#print(player)

		count += 1
		print(player.board)
	except Exception as e:
		print(player.direction)
		print(player.board)
		print(len(player.unique_loc)+1)
		print(e)

print(count)