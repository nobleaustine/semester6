import pandas as pd

t_table = pd.read_csv("inferential_statistics/t_table.csv")
print(t_table)

l = [14.3,12.6,13.7,10.9,13.7,12.0,11.4,12.0,12.6,13.1]
mean = sum(l)/len(l)
diff = [(x - mean)**2 for x in l]
sigma_2 = sum(diff)/len(diff)
sigma = sigma_2**0.5

print(mean)