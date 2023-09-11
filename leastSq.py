import numpy as np

def linear_regression_least_squares(X, y):
    '''
    Perform linear regression using the least squares method.

    Parameters:
    X: numpy.ndarray
        Input features matrix with shape (n_samples, n_features).
    y: numpy.ndarray
        Target values vector with shape (n_samples,).

    Returns:
    coefficients: numpy.ndarray
        Coefficients (weights) of the linear regression model.
    '''

    # Add a column of ones to the feature matrix to represent the intercept term
    ones_column = np.ones((X.shape[0], 1))
    X = np.hstack((ones_column, X))

    # Calculate the coefficients (weights) using the least squares formula
    coefficients = np.linalg.lstsq(X, y, rcond=None)[0]

    return coefficients

# Example usage:
# Generate some sample data
np.random.seed(0)
X = 2 * np.random.rand(100, 1)
y = 4 + 3 * X + np.random.randn(100, 1)

# Perform linear regression
coefficients = linear_regression_least_squares(X, y)

# The first coefficient is the intercept, and the second is the slope
intercept, slope = coefficients[0], coefficients[1]

print("Intercept:", intercept)
print("Slope:", slope)
