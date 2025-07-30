#multiplication table using for and while loops
x = int(input("Enter the number you want the multiplication table of:"))
for i in range(1, 11):
    print(f"{x} x {i} = {x * i}")
else:
    print("Multiplication table completed.")

#using while loop

x = int(input("Enter the number you want the multiplication table of:"))
i = 1
while i <= 10:
    print(f"{x} x {i} = {x * i}")
    i += 1
else:
    print("Multiplication table completed.")