# finally is mainly used in the context of exception handling in Python.
# mainly under functions.

def divide_numbers(a, b):
    try:
        result = a / b
    except ZeroDivisionError:
        print("Error: Division by zero is not allowed.")
        return None
    else:
        print(f"{a} divided by {b} gives: {result}")
    finally:
        print("Execution of divide_numbers completed.")

divide_numbers(10, 2)

divide_numbers(10, 0)
