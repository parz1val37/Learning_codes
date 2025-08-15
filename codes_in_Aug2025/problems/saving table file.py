
x = int(input("Enter the number u want the table of: "))

table = [x*i for i in range(1, 11)]
print(f"Table of {x} in a list is:\n{table}")

with open("Tables.txt", "a") as file:
    file.write(f"The table of {x} in a list is: {str(table)}\n")