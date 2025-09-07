import sympy as sp
# Defining variable
x = sp.Symbol('x')

print("\t\t\t\t⟪   LET'S DIFFERENCIATE    ⟫")
print("➡️  General equation for upto 3rd degree polynomial is 👉  ax³ + bx² + cx + d  👈")
print("➡️  You can make a=0 if you want to differeciate a quadratic and like wise (a=0 and b=0) for linear equation.")

a = float(input("Enter the value of a: "))
b = float(input("Enter the value of b: "))
c = float(input("Enter the value of c: "))
d = float(input("Enter the value of d: "))

try:
    expr = f"{(a)*x**3} {'+' if b>=0 else '-'} {abs(b)*x**2} {'+' if c>=0 else '-'} {abs(c)*x**1} {'+' if d>=0 else '-'} {abs(d)}"
    # print(expr)
    poly = sp.sympify(expr)  # convert string to sympy expression

    # First, second, and third derivatives
    replace = {"x**2": "x²", "*" : ""}

    first = sp.diff(poly, x, 1)
    fd1 = str(first)
    for old, new in replace.items():
        fd1 = fd1.replace(old, new)

    second = sp.diff(poly, x, 2)
    fd2 = str(second)
    fd2 = fd2.replace('*', '')

    third = sp.diff(poly, x, 3)
    # fd3 = str(third)
    # for old, new in replace.items():
    #     fd3 = fd3.replace(old, new)

    # print(f"\nGiven function:")
    print(f"\nFirst derivative (dy/dx): {fd1}")
    print(f"\nSecond derivative (d²y/dx²): {fd2}")
    print(f"\nThird derivative (d³y/dx³): {float(third)}")

except Exception as e:
    print(f"Error: {e}")