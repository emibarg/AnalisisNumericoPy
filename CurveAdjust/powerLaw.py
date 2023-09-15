import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from scipy.optimize import curve_fit

# Given data points
xi = np.array([1, 2, 3])  # X values
yi = np.array([1, 2.7182, 7.3891])  # Y values

# Define the power-law model function
def power_law_model(x, a, b):
    return a * (x ** b)

# Fit the power-law model to the data
params, covariance = curve_fit(power_law_model, xi, yi)

# Extract the estimated parameters
a, b = params

# Create a DataFrame to display the calculations step by step
data = {'xi': xi, 'yi': yi, 'log(xi)': np.log(xi), 'log(yi)': np.log(yi)}
df = pd.DataFrame(data)
df['log(xi)'] = df['log(xi)'].round(2)
df['log(yi)'] = df['log(yi)'].round(2)

# Print the DataFrame
print("Data and Calculations:")
print(df)

# Print the estimated parameters
print(f"\nEstimated 'a' parameter: {a:.4f}")
print(f"Estimated 'b' parameter: {b:.4f}")

# Plot the original data and the fitted power-law curve
plt.scatter(xi, yi, label='Original Data')
x_fit = np.linspace(min(xi), max(xi), 100)
y_fit = power_law_model(x_fit, a, b)
plt.plot(x_fit, y_fit, 'r-', label='Fitted Curve')
plt.xlabel('X')
plt.ylabel('Y')
plt.legend()
plt.grid(True)
plt.show()
