import numpy as np

file1 = open("my_file.csv", "r").read()
count = 0
file1 = file1.split("\n")

#MAS seem to be only cross shaped.
#So one having the indicies [i][j], [i+1][j+1], [i+2][j+2]
#and the other [i][j+2],[i+1][j+1],[i+2][j]
#11,12,13
#21,22,23
#31,32,33

for i in range(len(file1)-2):
	for j in range(len(file1[i])-2):
		if not file1[i+1][j+1] == "A":
			continue;

		masl = (file1[i][j]=="M" and file1[i+1][j+1]=="A" and file1[i+2][j+2]=="S")
		masr = (file1[i][j+2]=="M" and file1[i+1][j+1]=="A" and file1[i+2][j]=="S")
		saml = (file1[i][j]=="S" and file1[i+1][j+1]=="A" and file1[i+2][j+2]=="M")
		samr = (file1[i][j+2]=="S" and file1[i+1][j+1]=="A" and file1[i+2][j]=="M")

		if masl and masr:
			count += 1

		elif saml and samr:
			count += 1

		elif masl and samr:
			count += 1

		elif saml and masr:
			count += 1

print(count)