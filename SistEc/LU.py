import numpy as np

def lu_decomposition(A, b):
    '''
    Perform LU decomposition of a square matrix A and solve for y and x.

    Parameters:
    A: numpy.ndarray
        Coefficient matrix (square).
    b: numpy.ndarray
        Right-hand side vector.

    Returns:
    L: numpy.ndarray
        Lower triangular matrix.
    U: numpy.ndarray
        Upper triangular matrix.
    y: numpy.ndarray
        Solution to Ly = b.
    x: numpy.ndarray
        Solution to Ux = y.
    '''

    n = A.shape[0]
    L = np.eye(n)
    U = A.copy()
    y = np.zeros(n)
    x = np.zeros(n)

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

    # Solve Ly = b
    for i in range(n):
        y[i] = b[i] - np.dot(L[i, :i], y[:i])

    # Solve Ux = y
    for i in range(n - 1, -1, -1):
        x[i] = (y[i] - np.dot(U[i, i+1:], x[i+1:])) / U[i, i]

    return L, U, y, x

# Example usage:
A = np.array([[2, 1, -1],
              [1, 3, 2],
              [3, 2, -3]], dtype=float)
b = np.array([2, 4, -3], dtype=float)

L, U, y, x = lu_decomposition(A, b)

print("\nLower Triangular Matrix L:")
print(L)
print("\nUpper Triangular Matrix U:")
print(U)
print("\nSolution for y:")
print(y)
print("\nSolution for x:")
print(x)
