import numpy as np
file1 = open("my_file.csv", "r").read()
count = 0
file1 = file1.split("\n\n")
rules = [line.split("|") for line in file1[0].split("\n")]
reports = [line.split(",") for line in file1[1].split("\n")]
correct_reports = []


# go over every report
for report in reports:
	failed = False
	#rules that apply
	applicaple = [rule for rule in rules if (rule[0] in report and rule[1] in report)]
	for rule in applicaple:
		if report.index(rule[0]) > report.index(rule[1]):
			failed = True
			break

	if not failed:
		correct_reports.append(report)

print(correct_reports)
for report in correct_reports:
	count += int(report[int(len(report)/2-1/2)])

print("part1",count)

def compare(item1, item2):
    return fitness(item1) - fitness(item2)
#part2
new_reports = []
for report in reports:
	failed = False
	#rules that apply
	applicaple = [rule for rule in rules if (rule[0] in report and rule[1] in report)]
	new_report = report
	print(report)
	while True:
		swapped = False
		for rule in applicaple:
			if new_report.index(rule[0]) > new_report.index(rule[1]):
				swapped = True
				failed = True
				tmp = new_report[report.index(rule[0])]
				new_report[report.index(rule[0])] = new_report[report.index(rule[1])]
				new_report[report.index(rule[1])] = tmp
		if not swapped or not failed:
			break;

	if failed:
		print(new_report)
		new_reports.append(new_report)

count_2 = 0
for report in new_reports:
	count_2 += int(report[int(len(report)/2-1/2)])

print(count_2)