import numpy as np

arr = np.array([1, 2, 3, 4, 5, 6])

n_arr = arr.reshape(2, 3)

print("Old array:")
print(arr)

print("New array:")
print(n_arr)