a = input("enter nos by space ")
b = a.split()
b = [int(item) for item in b]
sum = 0
for i in b :
    sum = sum + i
average = sum/len(b)
print(f"Sum of nos is {sum} \n6there average is {average}")
