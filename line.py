import numpy as np
import matplotlib.pyplot as plt

x_values = list(range(0, 11))
x_values = [x/10 for x in x_values]
y_values = [np.sin(x) for x in x_values]

plt.plot(x_values, y_values)
plt.xlabel('x')
plt.ylabel('y = sin(x)')
plt.title('Sine Function')
plt.show()