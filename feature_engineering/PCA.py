import numpy as np

# Sample data
data = np.array(
    [
        [2.5, 0.5, 2.2, 1.9, 3.1, 2.3, 2, 1, 1.5, 1.1],
        [2.4, 0.7, 2.9, 2.2, 3, 2.7, 1.6, 1.1, 1.6, 0.9],
    ]
)
data = np.transpose(data)

# Step 1: Calculate mean
mean_values = np.mean(data, axis=0)
a1 = np.full(10, mean_values[0])
a2 = np.full(10, mean_values[1])

means = np.array([a1, a2])
means = np.transpose(means)
# Step 2: Subtract mean from the data
centered_data = data - means

# Step 3: Calculate covariance matrix
covariance_matrix_new = centered_data.T @ centered_data
covariance_matrix = np.cov(centered_data, rowvar=False)

# Step 4: Eigenvalue decomposition
eigenvalues, eigenvectors = np.linalg.eig(covariance_matrix)

# Display results
print("Original Data:")
print(data)

print("\nStep 1: Mean Values:")
print(mean_values)

print("\nStep 2: Centered Data:")
print(centered_data)

print("\nStep 3: Covariance Matrix:")
print(covariance_matrix)

print("\nStep 4: Eigenvalues:")
print(eigenvalues)

print("\nEigenvectors:")
print(eigenvectors)
