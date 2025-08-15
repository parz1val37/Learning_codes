
x = int(input("Enter the number u want the table of: "))

# table = [f"{x} x {i} = {x * i}" for i in range(1, 11)]
table = [x*i for i in range(1, 11)]

print(f"Table of {x} in a list is:\n{table}")