import matplotlib.pyplot as plt
import numpy as np
import pandas as pd

# Given data points
xi = np.array([1, 2, 2.5, 4, 6, 8, 8.5])# X values
yi = np.array([0.4, 0.7, 0.8, 1, 1.2, 1.3, 1.4])  # Y values

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

# Create a scatter plot of the data
plt.scatter(xi, yi)

# Add the best-fit line to the plot
x = np.linspace(np.min(xi), np.max(xi), 100)
y = m * x + b
plt.plot(x, y, color='red')

# Add labels and a title to the plot
plt.xlabel('X')
plt.ylabel('Y')
plt.title('Linear Regression')

# Show the plot
plt.show()