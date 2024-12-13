import numpy as np
import pandas as pd

df = pd.read_csv('my_file.csv', sep='   ', header=None)
df[0] = sorted(df[0])
df[1] = sorted(df[1])

similarity = []

for i in df[0]:
	amount = list(df[1]).count(i)
	similarity.append(i * amount)


print(sum(similarity))

print(sum(np.abs(df[1]-df[0])))