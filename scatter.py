import matplotlib.pyplot as plt
import numpy as np

# Create two lists of 50 random floating-point numbers between 0 and 1
x = np.random.rand(50)
y = np.random.rand(50)

# Plot a scatter plot of y against x
plt.scatter(x, y)

# Label the x-axis as 'x' and the y-axis as 'y'
plt.xlabel('x')
plt.ylabel('y')

# Add a title to the plot as 'Random Data Scatter Plot'
plt.title('Random Data Scatter Plot')

# Show the plot
plt.show()