import numpy as np

arr = np.array([
    [1, 2, 3],
    [5, 5, 5],
    [2, 2, 2]
])

row_sums = np.sum(arr, axis=1)

max_row_index = np.argmax(row_sums)

print("Row with the largest sum:", max_row_index)
