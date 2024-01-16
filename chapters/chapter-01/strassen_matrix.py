import numpy as np

def strassen_matrix_multiply(A, B):
    # Base case: if the matrices are 1x1, perform simple multiplication
    if len(A) == 1:
        return [[A[0][0] * B[0][0]]]

    # Matrix dimensions
    n = len(A)
    m = n // 2

    # Divide matrices into submatrices
    A11 = [row[:m] for row in A[:m]]
    A12 = [row[m:] for row in A[:m]]
    A21 = [row[:m] for row in A[m:]]
    A22 = [row[m:] for row in A[m:]]

    B11 = [row[:m] for row in B[:m]]
    B12 = [row[m:] for row in B[:m]]
    B21 = [row[:m] for row in B[m:]]
    B22 = [row[m:] for row in B[m:]]

    # Recursive steps for Strassen's algorithm
    P1 = strassen_matrix_multiply(A11, subtract_matrices(B12, B22))
    P2 = strassen_matrix_multiply(add_matrices(A11, A12), B22)
    P3 = strassen_matrix_multiply(add_matrices(A21, A22), B11)
    P4 = strassen_matrix_multiply(A22, subtract_matrices(B21, B11))
    P5 = strassen_matrix_multiply(add_matrices(A11, A22), add_matrices(B11, B22))
    P6 = strassen_matrix_multiply(subtract_matrices(A12, A22), add_matrices(B21, B22))
    P7 = strassen_matrix_multiply(subtract_matrices(A11, A21), add_matrices(B11, B12))

    # Calculate the result submatrices
    C11 = add_matrices(subtract_matrices(add_matrices(P5, P4), P2), P6)
    C12 = add_matrices(P1, P2)
    C21 = add_matrices(P3, P4)
    C22 = subtract_matrices(subtract_matrices(add_matrices(P5, P1), P3), P7)

    # Combine the result submatrices into the final result
    result = [[0] * n for _ in range(n)]
    for i in range(m):
        for j in range(m):
            result[i][j] = C11[i][j]
            result[i][j + m] = C12[i][j]
            result[i + m][j] = C21[i][j]
            result[i + m][j + m] = C22[i][j]

    return result

def add_matrices(A, B):
    return [[A[i][j] + B[i][j] for j in range(len(A[0]))] for i in range(len(A))]

def subtract_matrices(A, B):
    return [[A[i][j] - B[i][j] for j in range(len(A[0]))] for i in range(len(A))]

# Example usage:
A = [[1, 2], [3, 4]]
B = [[5, 6], [7, 8]]
result = strassen_matrix_multiply(A, B)
print("Matrix A:")
print(np.array(A))
print("\nMatrix B:")
print(np.array(B))
print("\nResult of Matrix Multiplication:")
print(np.array(result))
