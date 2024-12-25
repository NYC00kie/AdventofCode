import numpy as np

file1 = open("my_file.csv", "r").read().split("\n")
file1 = [[int(line.split(":")[0]),[int(x) for x in line.split(" ")[1:]]] for line in file1]
count = []
print(file1)

def doboth(goal,current_num,leftover_nums,i):
	# print(current_num,goal,leftover_nums,i)
	if len(leftover_nums) == 0:
		return current_num

	next_mul = current_num * leftover_nums[0]
	next_add = current_num + leftover_nums[0]
	next_con = int(str(current_num)+str(leftover_nums[0]))
	i += 1
	num1 = doboth(goal,next_mul,leftover_nums[1:],i)
	num2 = doboth(goal,next_add,leftover_nums[1:],i)
	num3 = doboth(goal,next_con,leftover_nums[1:],i)

	if num1 == goal:
		return num1
	elif num2 == goal:
		return num2
	elif num3 == goal:
		return num3
	else:
		return False

for line in file1:
	print(line)
	if line[0] == doboth(int(line[0]),line[1][0],line[1][1:],0):
		count.append(line[0])

print(count)
print(sum(count))