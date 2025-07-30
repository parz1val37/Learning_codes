n = int(input("Enter the number you want the factorial of: "))

fctrl = 1

if n < 0:
    print("Factorial is not defined for negative numbers.")
elif n == 0:
    print("The factorial of 0 is 1")
else:
    for i in range(1, n + 1):
        fctrl *= i
    print(f"The factorial of {n} is {fctrl}")

#factorial using for loop and if statement to handle negative input