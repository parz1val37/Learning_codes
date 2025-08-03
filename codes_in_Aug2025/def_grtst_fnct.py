def greatest():
    x = float(input("Enter first number: "))
    y = float(input("Enter second number: "))
    z = float(input("Enter third number: "))
    if x >= y and x >= z:
        print(f"Greatest number among entered number is {x}") 
    elif y >= x and y >= z:
        print(f"Greatest number among entered number is {y}")
    else:
        print(f"Greatest number among entered number is {z}")
    
greatest()  # calling the function greatest to execute the code inside it

