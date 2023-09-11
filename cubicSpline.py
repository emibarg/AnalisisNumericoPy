import numpy as np
from scipy.interpolate import CubicSpline
import matplotlib.pyplot as plt

# Define the data points
x_data = np.array([1.0, 2.0, 3.0, 4.0, 5.0])
y_data = np.array([0.0, 1.0, 0.0, 1.0, 0.0])

# Create a cubic spline interpolation
cs = CubicSpline(x_data, y_data, bc_type='natural')

# Define the range of x-values for interpolation
x_interp = np.linspace(min(x_data), max(x_data), 100)
y_interp = cs(x_interp)

# Plot the original data and the cubic spline interpolation
plt.scatter(x_data, y_data, label='Data')
plt.plot(x_interp, y_interp, label='Cubic Spline', color='red')
plt.xlabel('X')
plt.ylabel('Y')
plt.legend()
plt.show()
