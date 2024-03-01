import numpy as np
from scipy.stats import iqr

data = np.array(
    [23, 24, 26, 15, 13, 31, 42, 10, 11, 14, 16, 25, 48, 64, 93, 96, 72, 62, 52, 32, 28]
)
data = np.sort(data)
print(data)
m = np.median(data)
print(m)

# Calculate the first quartile (Q1)
Q1 = np.percentile(data, 25)

# Calculate the third quartile (Q3)
Q3 = np.percentile(data, 75)

# Calculate the Interquartile Range (IQR)
IQR = Q3 - Q1

print("Interquartile Range (IQR):", IQR)


# Sample data
data = [
    23,
    24,
    26,
    15,
    13,
    31,
    42,
    10,
    11,
    14,
    16,
    25,
    48,
    64,
    93,
    96,
    72,
    62,
    52,
    32,
    28,
]

# Calculate the Interquartile Range (IQR)
IQR = iqr(data)

print("Interquartile Range (IQR):", IQR)
