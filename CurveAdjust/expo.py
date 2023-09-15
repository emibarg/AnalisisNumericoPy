import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from scipy.optimize import curve_fit

# Given data points
xi = np.array([0, 1, 2, 3])  # X values
yi = np.array([1,2.7182, 7.3891, 20.0855])  # Y values

# Define the exponential model function
def exponential_model(x, a, b):
    return a * np.exp(b * x)

# Fit the exponential model to the data
params, covariance = curve_fit(exponential_model, xi, yi)

# Extract the estimated parameters
a, b = params

# Create a DataFrame to display the calculations step by step
data = {'xi': xi, 'yi': yi, 'ln(yi)': np.log(yi)}
df = pd.DataFrame(data)
df['ln(yi)'] = df['ln(yi)'].round(2)

# Print the DataFrame
print("Data and Calculations:")
print(df)

# Print the estimated parameters
print(f"\nEstimated 'a' parameter: {a:.2f}")
print(f"Estimated 'b' parameter: {b:.2f}")

# Plot the original data and the fitted exponential curve
plt.scatter(xi, yi, label='Original Data')
x_fit = np.linspace(min(xi), max(xi), 100)
y_fit = exponential_model(x_fit, a, b)
plt.plot(x_fit, y_fit, 'r-', label='Fitted Curve')
plt.xlabel('X')
plt.ylabel('Y')
plt.legend()
plt.grid(True)
plt.show()
