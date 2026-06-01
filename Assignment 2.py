"""" (a). Generate N = 25 random uniform integers from the set S = [−7, 3) = {𝑛 ∈ ℤ | − 7 ≤ 𝑛 < 3}, and store
these values in a 1D horizontal tensor 𝐇𝟏. Hint: You may find the function np.random.randint from the
NumPy library useful"""

import numpy as np

H1 = np.random.randint(-7,3, size=(1,25))
print (H1)

""" (b). Output the shape and size of 𝐇𝟏. Note: Think of 𝐇𝟏 as a matrix (not a vector)."""

print ("Shape of Vector:", H1.shape)
print ("Size of Vector:", H1.size)

""" (c). Create a new horizontal 1D tensor 𝐇𝟐 that store the entries of 𝐇𝟏 in the reverse order (i.e., [1, 2, 3]
becomes [3, 2, 1]). Find the shape and size of 𝐇𝟐. Note: Again, think of 𝐇𝟐 as a matrix (not a vector)"""

H2 = H1[:, ::-1]
print("Reverse of H1 is" ,H2)

""" (d). Change the 1D horizontal tensors 𝐇𝟏 and 𝐇𝟐 into 1D vertical tensors 𝐕𝟏 and 𝐕𝟐. Find the shape and size
of 𝐕𝟏 and 𝐕𝟐"""

V1 = H1.T
V2 = H2.T
print ("Vertical of H1:", V1)
print("Vertical of H2:", V2)
print("Shape of V1 =", V1.shape)
print("Size of V1 =", V1.size)
print("Shape of V2 =", V2.shape)
print("Size of V2 =", V2.size)

""" (e). Assuming we think of 𝐇𝟏 and 𝐇𝟐 as vectors, then apply their dot product using matrices 𝐕𝟏 and 𝐕𝟐 by
way of matrix multiplication. Store the result in D and find its shape and size"""
D = np.matmul(V1.T, V2)
print("Dot Product of V1 and V1 =" , D)
print("Shape of D = ", D.shape)
print("Size of D = ", D.size)

""" (f). Assuming we think of 𝐇𝟏 and 𝐇𝟐 as vectors, then, find the cosine similarity C. Hint: You may find the
function np.linalg.norm from the NumPy library useful.  """


dot = np.dot(H1.flatten(), H2.flatten())
norm1 = np.linalg.norm(H1)
norm2 = np.linalg.norm(H2)

C = dot / (norm1 * norm2)

print(C)

"""" (g) Do the vectors 𝐇𝟏 and 𝐇𝟐 have low, neutral, or high similarity? Explain your logic."""
"""The similarity between H1 and H2 is low to moderate because H₂ is just H₁ in reverse order. 
Even though they have the same numbers, they are not in the same positions,so they don’t line up well when compared. 
This leads to a lower cosine similarity"""

""" (h) Perform these matrix multiplications. What can you observe from the results? Explain your logic using
mathematical justifications.
𝐕𝟏 𝐕𝟐𝐓 =  (25×1) × (1×25) → (25×25) 
It represents the outer product.
V𝟐𝐓 𝐕𝟏 = (1×25) × (25×1) → (1×1) it is a dot product 
𝐕𝟐 𝐕𝟏𝐓 = (25×1) × (1×25) → (25×25) but the order of elements also matter so its not the same as V1V2T
"""
"""Write a Python script that inputs “N” (no. of generated integers) and “S” (the set from which values are
generated) and it outputs the results of (a) to (h). Your code should be written in a generic way in such a
way that it works for any feasible input “N” and “S” """

# -------- INPUT --------
# Ask user for number of integers
N = int(input("Enter number of integers (N): "))

# Ask user for start of range (inclusive)
S_start = int(input("Enter start of range (inclusive): "))

# Ask user for end of range (exclusive)
S_end = int(input("Enter end of range (exclusive): "))


# -------- (a) Create H1 --------
# Generate a 1×N matrix with random integers from S_start to S_end-1
H1 = np.random.randint(S_start, S_end, size=(1, N))

# Print H1 values
print("\nH1:", H1)

# Print shape (rows, columns)
print("H1 Shape:", H1.shape)

# Print total number of elements
print("H1 Size:", H1.size)


# -------- (c) Create H2 (reverse of H1) --------
# Reverse the order of elements in H1 (left to right)
H2 = H1[:, ::-1]

# Print H2 values
print("\n Reverse of H1 i.e. H2:", H2)

# Print shape and size (same as H1)
print("H2 Shape:", H2.shape)
print("H2 Size:", H2.size)


# -------- (d) Convert to vertical tensors --------
# Transpose H1 → converts row (1×N) into column (N×1)
V1 = H1.T

# Transpose H2 → also becomes (N×1)
V2 = H2.T

# Print V1
print("\nV1:\n", V1)
print("V1 Shape:", V1.shape)
print("V1 Size:", V1.size)

# Print V2
print("\nV2:\n", V2)
print("V2 Shape:", V2.shape)
print("V2 Size:", V2.size)


# -------- (e) Dot Product using matrix multiplication --------
# V1.T = (1×N), V2 = (N×1)
# Result = (1×1) → single value (dot product)
D = np.matmul(V1.T, V2)

print("\nDot Product of V1 V2 is D:", D)
print("D Shape:", D.shape)
print("D Size:", D.size)


# -------- (f) Cosine Similarity --------
# Flatten converts (1×N) matrix → 1D vector (N,)
dot = np.dot(H1.flatten(), H2.flatten())  # compute dot product

# Compute magnitude (length) of each vector
norm1 = np.linalg.norm(H1)
norm2 = np.linalg.norm(H2)

# Apply cosine similarity formula
C = dot / (norm1 * norm2)

print("\nCosine Similarity C:", C)


# -------- Matrix Multiplications --------

# (1) V1 × V2^T → (N×1)(1×N) = (N×N)
# Outer product (every element multiplied with every other)
M1 = np.matmul(V1, V2.T)
print("\nV1 V2^T:\n", M1)
print("Shape:", M1.shape)


# (2) V2^T × V1 → (1×N)(N×1) = (1×1)
# This is the dot product again
M2 = np.matmul(V2.T, V1)
print("\nV2^T V1:\n", M2)
print("Shape:", M2.shape)


# (3) V2 × V1^T → (N×1)(1×N) = (N×N)
# Another outer product (different order → different matrix)
M3 = np.matmul(V2, V1.T)
print("\nV2 V1^T:\n", M3)
print("Shape:", M3.shape)

""" Question 2 Write a Python script that inputs “N” and “S” like above, and it outputs four matrices as shown below. Matrices
1 and 2 will have the entries in the main diagonal and zeros everywhere else. Matrix 3 will superimpose Matrix
1 and 2 and have zero entries everywhere else (note: add entries that overlap). Matrix 4 has a serpent-like shape,
and the resultant matrix will have N entries"""

# -------- INPUT --------
N = int(input("Enter N (must be perfect square): "))
S_start = int(input("Enter start of range: "))
S_end = int(input("Enter end of range: "))

# Generate N random values
values = np.random.randint(S_start, S_end, size=N)

# Matrix size
n = int(np.sqrt(N))

# -------- Matrix 1 (main diagonal) --------
M1 = np.zeros((n, n), dtype=int)

for i in range(n):
    M1[i, i] = values[i]

print("\nMatrix 1:\n", M1)
print("Shape:", M1.shape, "Size:", M1.size)


# -------- Matrix 2 (other diagonal) --------
M2 = np.zeros((n, n), dtype=int)

for i in range(n):
    M2[i, n - 1 - i] = values[i]

print("\nMatrix 2:\n", M2)
print("Shape:", M2.shape, "Size:", M2.size)


# -------- Matrix 3 (sum of both) --------
M3 = M1 + M2

print("\nMatrix 3:\n", M3)
print("Shape:", M3.shape, "Size:", M3.size)


# -------- Matrix 4 (serpent pattern) --------
M4 = np.zeros((n,n), dtype = int)

index = 0

for j in range(n):  # column-wise
    if j % 2 == 0:
        # top to bottom
        for i in range(n):
            M4[i, j] = values[index]
            index += 1
    else:
        # bottom to top
        for i in range(n - 1, -1, -1):
            M4[i, j] = values[index]
            index += 1

print("\nMatrix 4:\n", M4)
print("Shape:", M4.shape, "Size:", M4.size)
