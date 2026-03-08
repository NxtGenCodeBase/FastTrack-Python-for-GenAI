import numpy as np

# Create a 2D array
arr = np.array([[1, 2, 3], [4, 5, 6]])

# Broadcasting: Add a scalar to the entire array
print(arr + 10)

# Slicing: Get the first column of all rows
print(arr[:, 0])

# Reshaping for AI (common for image data or features)
vector = np.arange(12)
matrix = vector.reshape(3, 4)
print(f"Reshaped Matrix:\n{matrix}")
