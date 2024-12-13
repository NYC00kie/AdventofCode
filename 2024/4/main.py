#2500 too low
#2550 too high

import numpy as np
file1 = open("my_file.csv", "r").read()
count = 0
file1 = file1.split("\n")
file2 = ["".join(line) for line in np.rot90([list(line) for line in file1])]
count += sum([line.count("SAMX") for line in file1])
count += sum([line.count("XMAS") for line in file1])
count += sum([line.count("SAMX") for line in file2])
count += sum([line.count("XMAS") for line in file2])
# left to right and up and down

print(count)
for i in range(len(file1)-3):
	for j in range(len(file1[i])-3):
		if file1[i][j] == "X" and file1[i+1][j+1] == "M" and file1[i+2][j+2] == "A" and file1[i+3][j+3] == "S":
			count += 1
			print(i,j)
		elif file1[i][j] == "S" and file1[i+1][j+1] == "A" and file1[i+2][j+2] == "M" and file1[i+3][j+3] == "X":
			count += 1
			print(i,j)
print(count)
for i in range(len(file1)-3):
	for j in range(3,len(file1[i])):
		print(1,count)
		if file1[i][j] == "X" and file1[i+1][j-1] == "M" and file1[i+2][j-2] == "A" and file1[i+3][j-3] == "S":
			count += 1
			print(i,j)
		elif file1[i][j] == "S" and file1[i+1][j-1] == "A" and file1[i+2][j-2] == "M" and file1[i+3][j-3] == "X":
			count += 1
			print(i,j)
		print(2,count)


print(count)