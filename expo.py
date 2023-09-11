import numpy as np
import matplotlib.pyplot as plt
from scipy.optimize import curve_fit

# Define the exponential function model
def exponential_model(x, a, b, c):
    return a * np.exp(b * x) + c

# Generate some sample data
x_data = np.array([0, 1, 2, 3, 4, 5])
y_data = np.array([1, 3, 8, 20, 48, 120])

# Fit the exponential model to the data
params, covariance = curve_fit(exponential_model, x_data, y_data)

# Extract the parameters (a, b, c) from the fitting
a, b, c = params

# Predict values using the fitted model
y_fit = exponential_model(x_data, a, b, c)

# Plot the original data and the fitted curve
plt.scatter(x_data, y_data, label='Data')
plt.plot(x_data, y_fit, label='Fitted Curve', color='red')
plt.xlabel('X')
plt.ylabel('Y')
plt.legend()
plt.show()

# Print the fitted parameters
print(f'Fitted Parameters: a={a}, b={b}, c={c}')
