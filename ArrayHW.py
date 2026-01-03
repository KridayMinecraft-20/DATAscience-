import numpy as np

arr = np.linspace(0, 9, 10, dtype=int)
print("Original array:")
print(arr)

modified_arr = np.where(arr % 2 != 0, -1, arr)
print("\nArray after replacing odd numbers with -1:")
print(modified_arr)

two_d_arr = arr.reshape(2, 5)
print("\n2D array with two rows:")
print(two_d_arr)


even_sum = 0
for num in arr:
    if num % 2 == 0:
        even_sum += num

print("\nSum of all even numbers in the original array:")
print(even_sum)
