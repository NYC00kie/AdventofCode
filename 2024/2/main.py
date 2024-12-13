file1 = open("my_file.csv", "r").readlines()


my_data = [[int(num) for num in part[:-1].split(" ")] for part in file1]

print(my_data)

sorted_reports = []

for a in my_data:
	#ascend
	val1 = all(a[i] < a[i + 1] for i in range(len(a) - 1))
	#descending
	val2 = all(a[i] > a[i + 1] for i in range(len(a) - 1))
	val = bool(val1+val2)

	if val == True:
		sorted_reports.append(a)

correct_reports = 0

for report in sorted_reports:
	grad = [j-i for i, j in zip(report[:-1], report[1:])]

	val = all(x <= 3 and x >= -3 for x in grad)

	if val == True :
		correct_reports += 1

print(correct_reports)