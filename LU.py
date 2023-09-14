import numpy as np

def lu_decomposition(A):
    '''
    Perform LU decomposition of a square matrix A.

    Parameters:
    A: numpy.ndarray
        Coefficient matrix (square).

    Returns:
    L: numpy.ndarray
        Lower triangular matrix.
    U: numpy.ndarray
        Upper triangular matrix.
    '''

    n = A.shape[0]
    L = np.eye(n)
    U = A.copy()

    print("Initial Matrix:")
    print(U)

    for k in range(n - 1):
        for i in range(k + 1, n):
            factor = U[i, k] / U[k, k]
            L[i, k] = factor
            U[i, k:] -= factor * U[k, k:]
        
        print(f"\nStep {k + 1} - L Matrix:")
        print(L)
        print(f"\nStep {k + 1} - U Matrix:")
        print(U)

    return L, U

# Example usage:
A = np.array([[2, 1, -1],
              [1, 3, 2],
              [3, 2, -3]], dtype=float)

L, U = lu_decomposition(A)

print("\nLower Triangular Matrix L:")
print(L)
print("\nUpper Triangular Matrix U:")
print(U)
