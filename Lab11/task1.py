import numpy as np

arr = np.array([12, 5, 8, 1, 19, 3, 7, 2])

k = 3

smallest = np.partition(arr, k - 1)[:k]

print("K-smallest values:")
print(smallest)