# test python code snippets

import numpy as np
import pandas as pd

# Create a 3D NumPy array
array_3d = np.array(
    [[[1, 2, 3], [4, 5, 6]], [[7, 8, 9], [10, 11, 12]], [[13, 14, 15], [16, 17, 18]]]
)

# Reshape the 3D array into a 2D array
reshaped_array = array_3d.reshape(
    -1, array_3d.shape[-1]
)  # Reshape along the last dimension
print("2D array from 3D array:")
print(reshaped_array)

# Define row names and column names for the DataFrame
row_names = ["Row" + str(i + 1) for i in range(array_3d.shape[0])]
column_names = ["Column" + str(j + 1) for j in range(array_3d.shape[-1])]

# Create a DataFrame from the reshaped 2D array with row and column names
df = pd.DataFrame(reshaped_array, index=row_names, columns=column_names)

print("\nDataFrame from reshaped 2D array with named rows and columns:")
print(df)
