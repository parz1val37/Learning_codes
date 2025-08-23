import math
print("General form of quadratic is: ax^2 + bx + c, where (a!=0).")
a = int(input("Enter the value for a: "))
if a == 0:
    print("Error: 'a' can't be equals to zero.")
else:
    b = int(input("Enter the value for b: "))
    c = int(input("Enter the value for c: "))
    if c == 0:
        print(f"The quadratic is: {a}x^2 + {b}x")
    else:
        print(f"The quadratic is: {a}x^2 + {b}x + {c}")

    d = b**2 - 4*a*c
    
    if d<0:
        d = d*(-1)
        x = str(2*a)
        print("This quadratic have complex roots.")
        root1 = (f"{(-1*b)} + i{round(math.sqrt(d), 2)}")
        root2 = (f"{(-1*b)} - i{round(math.sqrt(d), 2)}") 
        print(f"The roots of given quadratic are \'{root1}/{x}\' and \'{root2}/{x}\'.")
    
    elif d == 0:
        print("This quadratic have equal roots.")
        print(f"Which is \'{(-b/(2*a))}\'.")
    
    else:
        print("This quadratic have two real and distinct roots.")
        root1 = (-b + round(math.sqrt(d), 2))/(2*a)
        root2 = (-b - round(math.sqrt(d), 2))/(2*a)

        print(f"Which are \'{root1}\' and \'{root2}\'.")
