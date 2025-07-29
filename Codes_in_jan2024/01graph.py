import matplotlib.pyplot as plt
X_values = [1,5,3,4]
Y_values = [2,4,6,8]
plt.plot(X_values,Y_values , label='line')

plt.xlabel("X-axis")
plt.ylabel("Y-axis")
plt.title("LINE")
plt.legend()
k = plt.show()
print(k)