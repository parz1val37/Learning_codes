#factorials using recursion

def factorial(n):
    if n == 0 or n == 1:
        return 1
    else:
        return n * factorial(n - 1)   # return statement store value and print it when function is called
    
n = int(input("Enter a number to find its factorial: "))
print(f"The factorial of {n} is: {factorial(n)}")
