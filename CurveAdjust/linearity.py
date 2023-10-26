import matplotlib.pyplot as plt
import numpy as np

# Generate some random data
x = [1,2,3,4,5]
y = [0.5,1.7,3.4,5.7,8.4]

# Convert x to a NumPy array
x = np.array(x)

# Create a scatter plot
plt.scatter(x, y)
plt.xlabel('X')
plt.ylabel('Y')
plt.title('Scatter plot of X vs Y')

# Add a regression line to the plot
m, b = np.polyfit(x, y, 1)
plt.plot(x, m * x + b, color='red')

# Show the plot
plt.show()