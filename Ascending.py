import numpy as np
arr= np.array([1, 2, 3, 4, 5, 6, 7, 8, 9, 90, 89, 78])
print(arr[0])
print(arr[0:3])
print(arr.dtype)
newarr= arr.reshape(4,3)
print(newarr)
