import matplotlib.pyplot as plt

# Sample data
x = [1, 2, 3, 4, 5]
y1 = [2, 4, 6, 8, 10]
y2 = [1, 2, 1, 2, 1]

# Plotting the data
plt.plot(x, y1, label='Line 1')
plt.plot(x, y2, label='Line 2')

# Adding a legend
plt.legend()

# Adding labels and title
plt.xlabel('X-axis')
plt.ylabel('Y-axis')
plt.title('Example Plot with Legend')

# Display the plot
plt.show()
