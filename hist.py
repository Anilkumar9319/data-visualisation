import numpy as np
import matplotlib.pyplot as plt

# Generate 1000 normally distributed random numbers
data = np.random.normal(size=1000)

# Plot the histogram of the data
plt.hist(data, bins=20)

# Set the labels for the x-axis and y-axis
plt.xlabel('Value')
plt.ylabel('Frequency')

# Add a title to the plot
plt.title('Histogram of Randomly Generated Data')

# Display the plot
plt.show()