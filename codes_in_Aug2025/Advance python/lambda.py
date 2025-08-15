#-- using a normal function ---

# def square():
#     n = int(input("Enter the number to get it's square: "))
#     print(f"Square of {n} is: {n * n}")
# square()

#--- using lambda function ---

square = lambda n = int(input("Enter the number to get it's square: ")): print(f"Square of {n} is: {n * n}")
#--- here lambda takes 'n' :and returns/prints the square of 'n' ---
square()