import numpy as np

arr1 = np.array([10, 20, 30, 40, 50])
arr2 = np.array([10, 22, 30, 44, 50])

positions = np.where(arr1 == arr2)

print("Matching positions:")
print(positions)