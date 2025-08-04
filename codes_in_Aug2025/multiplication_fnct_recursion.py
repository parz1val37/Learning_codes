n = int(input("Enter the number you want multiplication table of: "))

def multiply(n, m=1):
    if m > 10:
        return
    else:
        print(f"{n} X {m} = {n * m}")
    multiply(n, m + 1)

multiply(n)
