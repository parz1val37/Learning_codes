print("Permutations of 'n' distinct objects taken 'r' at a time is given by:\nnPr = n!/(n-r)!, where \"!\" denotes the factorial.\n")


try:
    n = int(input("Enter the value of n (n>0): "))
    if n>0:
        r = int(input("Enter the value of r (r>=0): "))
    elif n<=0:
        print("Enter a valid input")
        exit()

    def factorial(x):
        if x==0 or x==1:
            return 1
        else:
            return x*factorial(x-1)

    ans = (factorial(n))/(factorial(n-r))
    print(f"\nPermutation of {n} distinct objects taken {r} at a time is: {int(ans)}")

except Exception as e:
    print(f"ERROR: {e}")