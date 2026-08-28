import numpy as np

arr = np.array([10, 20, 30, 20, 50])

value = 20

result = np.where(arr == value)

print("Positions of", value, ":", result)