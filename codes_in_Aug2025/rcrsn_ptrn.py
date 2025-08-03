def star_ptrn(n):
    if n == 0:
        return
    else:
        print("*" * n)
    star_ptrn(n - 1)
n = int(input("Enter the number of rows: "))
star_ptrn(n)
