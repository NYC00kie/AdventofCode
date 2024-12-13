#45877215 too low
#110348468 too high
#69230381 too high

import re
# r"mul\((\d{1,3}),(\d{1,3})\)"
file1 = open("my_file.csv", "r").read()

while True:
	dont_i = file1.find("don't()")
	do_i = file1.find("do()",dont_i)

	print(dont_i,do_i)
	if do_i == -1:
		file1 = file1[:dont_i]
		break;
	print(file1[dont_i:do_i+len("do()")])
	file1 = file1[:dont_i] + file1[do_i+len("do()"):]


res = 0
print(file1)
for element in re.finditer(r"mul\((\d{1,3}),(\d{1,3})\)",file1):
	res += int(element.group(1))*int(element.group(2))

print(res)