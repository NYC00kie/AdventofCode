file1 = open("my_file.csv", "r").readlines()


my_data = [[int(num) for num in part[:-1].split(" ")] for part in file1]

correct_reports = 0
for report in my_data: 
	val = False
	print(report,len(report)-1)
	all_possible = [report[:i]+report[i+1:] for i in range(len(report))]+[report]
	print(all_possible)
	for a in all_possible:
		val = all(a[i] < a[i + 1] for i in range(len(a) - 1)) or all(a[i] > a[i + 1] for i in range(len(a) - 1))
		print(val)
		if val == False:
			continue;

		diff = [j-i for i, j in zip(a[:-1], a[1:])]

		val = all(x <= 3 and x >= -3 for x in diff)

		if val == True :
			correct_reports += 1
			break;



print(correct_reports)