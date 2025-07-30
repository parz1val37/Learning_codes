#factorial using while loop
n = int(input("Enter the number you want the factorial of: "))
i = 1
factrl = 1

while i <= n:
    factrl *= i
    i += 1

print(f"The factorial of {n} is {factrl}")

#But it also give factorial of negative numbers which is not correct.