import matplotlib.pyplot as plt

a = input("enter x-values by space:")
x = a.split()
x = [int(item) for item in x]

b = input("enter y-values by space:")
y = b.split()
y = [int(item) for item in y]

print(f"X-values are {x} and Y-values are {y}\nloading graph:-")

plt.plot(x,y,label='CURVE')

plt.xlabel("X-axis")
plt.ylabel("Y-values")
plt.title("USER GRAPH")
plt.legend()

k = plt.show()

print(k)

