def star_ptrn(n):
    if n == 0:
        print("No pattern for zero row.")
        return
    elif n < 0:
        print("Negative intezers are not allowed.")
        return
    else:
        print("*" * n)
    star_ptrn(n - 1)
n = int(input("Enter the number of rows: "))
star_ptrn(n)

