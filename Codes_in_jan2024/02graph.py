import matplotlib.pyplot as plt
import numpy as np

def equation(x):
    return x**2

x_values = np.linspace(-6,6,1000)
y_values = equation(x_values)

plt.plot(x_values,y_values,label='curve')
plt.xlabel('X-axis')
plt.ylabel('Y-axis')
plt.title("CURVES")
plt.legend()

plt.show()