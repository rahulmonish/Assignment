import numpy as np
A = np.array([[3, 5, 6], [4, 8, 10], [2, 1, 8]])
I = np.array([[1, 0, 0], [0, 1, 0], [0, 0, 1]])

print(A.dot(I))