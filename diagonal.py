import numpy as np

# Set printoptions to use the legacy string formatting from NumPy 1.13  
np.set_printoptions(legacy='1.13')

# Take input for N and M, and create a NumPy array of shape (N, M) with all zeros
N, M = map(int, input().split())

# Create the NXM array with diagonal elements as 1 and others as 0
matrix = np.eye(N, M)

# Print the array
print(matrix)