import math
print("General form of quadratic is: ax^2 + bx + c, where (a!=0).")
try:
    a = float(input("Enter the value for a: "))
    if a == 0:
        print("a can't be equals to zero.")
    else:
        b = float(input("Enter the value for b: "))
        c = float(input("Enter the value for c: "))
        if c == 0:
            print(f"The quadratic is: {a}x² {'+' if b>0 else '-' } {abs(b)}x")
        elif b==0:
            print(f"The quadratic is: {a}x² {'+' if c>0 else '-' } {abs(c)}")
        else:
            print(f"The quadratic is: {a}x² {'+' if b>0 else '-' } {abs(b)}x {'+' if c>0 else '-' } {abs(c)}")

        d = b**2 - 4*a*c
        
        if d<0:
            print("This quadratic have complex roots.")
            if b==0:
                imag = round(((math.sqrt(-d))/(2*a)), 2)
                root1 = (f"i{imag}")
                root2 = (f"-i{imag}") 
                print(f"The roots of given quadratic are \'{root1}\' and \'{root2}\'.")
            else:
                real = round((-b)/(2*a), 2)
                imag = round(((math.sqrt(-d))/(2*a)), 2)
                root1 = (f"{real} + i{imag}")
                root2 = (f"{real} - i{imag}") 
                print(f"The roots of given quadratic are \'{root1}\' and \'{root2}\'.")
        elif d == 0:
            print("This quadratic have equal roots.")
            print(f"Which is \'{round((-b/(2*a)), 2)}\'.")
        
        else:
            print("This quadratic have two real and distinct roots.")
            root1 = round((-b + math.sqrt(d))/(2*a), 2)
            root2 = round((-b - math.sqrt(d))/(2*a), 2)
            print(f"Which are \'{root1}\' and \'{root2}\'.")
except Exception as e:
    print(f"ERROR: {e}")
