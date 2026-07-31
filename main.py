# Day 3 - NumPy: Arrays, Indexing, and Mathematical Operations
import numpy as np

# ============================================================
# 1. CREATING NUMPY ARRAYS
# ============================================================
print("=" * 60)
print("DAY 3: NUMPY FUNDAMENTALS")
print("=" * 60)

# From a list
arr1 = np.array([1, 2, 3, 4, 5])
print(f"\n1. Array from list: {arr1}")

# 2D array (matrix)
arr2d = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
print(f"\n2. 2D Array (Matrix):\n{arr2d}")

# Special arrays
zeros = np.zeros((3, 3))
print(f"\n3. Zeros Array:\n{zeros}")

ones = np.ones((2, 4))
print(f"\n4. Ones Array:\n{ones}")

range_arr = np.arange(0, 10, 2)  # start, stop, step
print(f"\n5. Range Array (0 to 10, step 2): {range_arr}")

linspace_arr = np.linspace(0, 1, 5)  # 5 evenly spaced numbers from 0 to 1
print(f"\n6. Linspace Array (0 to 1, 5 points): {linspace_arr}")

random_arr = np.random.randint(1, 100, size=(3, 4))
print(f"\n7. Random Integer Array (3x4):\n{random_arr}")

# ============================================================
# 2. ARRAY ATTRIBUTES
# ============================================================
print("\n" + "=" * 60)
print("ARRAY ATTRIBUTES")
print("=" * 60)

arr = np.array([[1, 2, 3, 4], [5, 6, 7, 8]])
print(f"\nArray:\n{arr}")
print(f"Shape: {arr.shape}")
print(f"Dimensions (ndim): {arr.ndim}")
print(f"Size (total elements): {arr.size}")
print(f"Data type (dtype): {arr.dtype}")
print(f"Item size (bytes): {arr.itemsize}")

# ============================================================
# 3. INDEXING AND SLICING
# ============================================================
print("\n" + "=" * 60)
print("INDEXING AND SLICING")
print("=" * 60)

arr = np.array([10, 20, 30, 40, 50, 60, 70, 80])
print(f"\nArray: {arr}")
print(f"First element: {arr[0]}")
print(f"Last element: {arr[-1]}")
print(f"Elements 2 to 5: {arr[2:6]}")
print(f"Elements from start to 4: {arr[:4]}")
print(f"Elements from 3 to end: {arr[3:]}")
print(f"Every other element: {arr[::2]}")
print(f"Reversed array: {arr[::-1]}")

# 2D indexing
arr2d = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
print(f"\n2D Array:\n{arr2d}")
print(f"Element at row 1, col 2: {arr2d[1, 2]}")
print(f"First row: {arr2d[0]}")
print(f"First column: {arr2d[:, 0]}")
print(f"Submatrix (rows 0-1, cols 1-2):\n{arr2d[0:2, 1:3]}")

# Boolean indexing
arr = np.array([1, 2, 3, 4, 5, 6, 7, 8, 9, 10])
print(f"\nArray: {arr}")
print(f"Elements > 5: {arr[arr > 5]}")
print(f"Even elements: {arr[arr % 2 == 0]}")

# ============================================================
# 4. MATHEMATICAL OPERATIONS
# ============================================================
print("\n" + "=" * 60)
print("MATHEMATICAL OPERATIONS")
print("=" * 60)

a = np.array([1, 2, 3, 4])
b = np.array([5, 6, 7, 8])

print(f"\nArray a: {a}")
print(f"Array b: {b}")
print(f"Addition (a + b): {a + b}")
print(f"Subtraction (a - b): {a - b}")
print(f"Multiplication (a * b): {a * b}")
print(f"Division (a / b): {a / b}")
print(f"Power (a ** 2): {a ** 2}")
print(f"Square root (sqrt): {np.sqrt(a)}")
print(f"Exponential (exp): {np.exp(a)}")

# Universal functions (ufuncs)
print(f"\nSum of a: {np.sum(a)}")
print(f"Mean of a: {np.mean(a)}")
print(f"Standard deviation of a: {np.std(a)}")
print(f"Min of a: {np.min(a)}")
print(f"Max of a: {np.max(a)}")

# ============================================================
# 5. BROADCASTING
# ============================================================
print("\n" + "=" * 60)
print("BROADCASTING")
print("=" * 60)

arr = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
scalar = 10
print(f"\nArray:\n{arr}")
print(f"Broadcasted with scalar {scalar}:\n{arr + scalar}")

# ============================================================
# 6. RESHAPING AND TRANSPOSING
# ============================================================
print("\n" + "=" * 60)
print("RESHAPING AND TRANSPOSING")
print("=" * 60)

arr = np.arange(1, 13)
print(f"\nOriginal array: {arr}")
print(f"Reshaped to 3x4:\n{arr.reshape(3, 4)}")
print(f"Reshaped to 4x3:\n{arr.reshape(4, 3)}")
print(f"Flattened (ravel): {arr.reshape(3, 4).ravel()}")

# ============================================================
# 7. LINEAR ALGEBRA OPERATIONS
# ============================================================
print("\n" + "=" * 60)
print("LINEAR ALGEBRA OPERATIONS")
print("=" * 60)

A = np.array([[1, 2], [3, 4]])
B = np.array([[5, 6], [7, 8]])
print(f"\nMatrix A:\n{A}")
print(f"Matrix B:\n{B}")
print(f"Matrix multiplication (dot):\n{np.dot(A, B)}")
print(f"Matrix transpose of A:\n{A.T}")
print(f"Determinant of A: {np.linalg.det(A):.2f}")
print(f"Inverse of A:\n{np.linalg.inv(A)}")

# Save output to file
with open("output.txt", "w", encoding="utf-8") as f:
    f.write("Day 3 - NumPy: Arrays, Indexing, and Mathematical Operations\n")
    f.write("Successfully completed all NumPy exercises!\n")

print("\n" + "=" * 60)
print("DAY 3 COMPLETED SUCCESSFULLY!")
print("=" * 60)
