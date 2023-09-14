import numpy as np

def gauss_seidel(A, b, x0, epsilon, max_iter):
    '''
    Solve a system of linear equations Ax = b using the Gauss-Seidel method.

    Parameters:
    A: numpy.ndarray
        Coefficient matrix.
    b: numpy.ndarray
        Right-hand side vector.
    x0: numpy.ndarray
        Initial guess for the solution.
    epsilon: float
        Convergence criteria: stop when the difference between consecutive
        iterates is less than epsilon.
    max_iter: int
        Maximum number of iterations.

    Returns:
    x: numpy.ndarray
        Solution vector.
    '''

    n = len(b)
    x = x0.copy()
    
    print("Initial Guess:")
    print(x)

    for k in range(max_iter):
        for i in range(n):
            x[i] = (b[i] - np.dot(A[i, :i], x[:i]) - np.dot(A[i, i+1:], x[i+1:])) / A[i, i]
        
        print(f"\nIteration {k + 1}:")
        print(x)

        if np.all(np.abs(A @ x - b) < epsilon):
            print(f"\nConverged after {k + 1} iterations.")
            return x

    print("\nExceeded maximum iterations.")
    return x

# Example usage:
A = np.array([[4, -1, 0, 3],
              [1, 15.5, 3, 8],
              [0, -1.3, -4, 1.1],
              [14, 5, -2, 30]], dtype=float)
b = np.array([1, 1, 1, 1], dtype=float)
x0 = np.zeros(len(b), dtype=float)
epsilon = 1e-6
max_iter = 50

x = gauss_seidel(A, b, x0, epsilon, max_iter)
print("\nSolution x:")
print(x)
