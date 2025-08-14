a = int(input("Enter a number: "))
b = int(input("Enter another number: "))

if b == 0:
    raise ZeroDivisionError("Division by zero is not allowed.")
else:
    result = a / b
    print(f"The result of {a} divided by {b} is {result}.")
