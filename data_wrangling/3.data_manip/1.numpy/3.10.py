import numpy as np


array_1 = np.arange(0,11)
print("Array:",array_1)

print("Element at 7th index is:", array_1[7])
print("Elements from 3rd to 5th index are:", array_1[3:6])
print("Elements up to 4th index are:", array_1[:4])

matrix_1 = np.random.randint(10,100,15).reshape(3,5)
print("Matrix of random 2-digit numbers\n ",matrix_1)

print("\nDouble bracket indexing\n")
print("Element in row index 1 and column index 2:", \
matrix_1[1][2])

print("\nSingle bracket with comma indexing\n")
print("Element in row index 1 and column index 2:", \
matrix_1[1,2])

print("\nRow or column extract\n")
print("Entire row at index 2:", matrix_1[2])
print("Entire column at index 3:", matrix_1[:,3])

print("\nSubsetting sub-matrices\n")
print("Matrix with row indices 1 and 2 and column "\
"indices 3 and 4\n", matrix_1[1:3,3:5])

print("Matrix with row indices 0 and 1 and column "\
"indices 1 and 3\n", matrix_1[0:2,[1,3]])

mat_1 = np.random.randint(10, 100, 15).reshape(3, 5)

print(f'Matrix of random 2-digit numbers\n{mat_1}')
print(f'\nElements greater than 50\n{mat_1[mat_1 > 50]}')

mat1 = np.random.randint(1,10, 9).reshape(3,3)
mat2 = np.random.randint(1,10, 9).reshape(3,3)

print(mat1 + mat2)
print(mat1 * mat2)
print(mat1 / mat2)
print(3*mat1 - 5*mat2)

# stacking arrays
a = np.random.randn(2,4)
b = np.random.randn(2, 4)
print(a)
print(b)
print(f'Vertical stacking\n{np.vstack((a,b))}')
print(f'Horizontal stacking\n{np.hstack([a,b])}')
