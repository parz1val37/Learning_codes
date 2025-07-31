n = int(input("enter a number: "))
print(f"reversed table of {n} is:")

#method 01:

for i in range(10, 0, -1):
    print(f"{n} X {i} = {n * i}")

#method 02:
x = int(input("Enter a number: "))
print(f"Reversed table of {x} is:")
for i in range(1, 11):
    print(f"{x} X {(11-i)} = {x *(11-i)}")

#Shows error for float input