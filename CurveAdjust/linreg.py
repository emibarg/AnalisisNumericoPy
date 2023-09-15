import numpy as np
import pandas as pd

# Given data points
xi = np.array([1, 2, 3, 4, 5])  # X values
yi = np.array([0, 1, 0, 1, 0])  # Y values

# Calculate the means of X and Y
mean_x = np.mean(xi)
mean_y = np.mean(yi)

# Calculate the slope (m) and intercept (b) of the best-fit line
numerator = np.sum((xi - mean_x) * (yi - mean_y))
denominator = np.sum((xi - mean_x) ** 2)
m = numerator / denominator
b = mean_y - m * mean_x

# Create a DataFrame to display the calculations step by step
data = {'xi': xi, 'yi': yi, 'xi - mean_x': xi - mean_x, 'yi - mean_y': yi - mean_y,
        '(xi - mean_x) * (yi - mean_y)': (xi - mean_x) * (yi - mean_y),
        '(xi - mean_x)^2': (xi - mean_x) ** 2}
df = pd.DataFrame(data)
df['(xi - mean_x) * (yi - mean_y)'] = df['(xi - mean_x) * (yi - mean_y)'].round(2)

# Print the DataFrame
print("Data and Calculations:")
print(df)

# Print the slope (m) and intercept (b)
print(f"\nSlope (m): {m:.2f}")
print(f"Intercept (b): {b:.2f}")
