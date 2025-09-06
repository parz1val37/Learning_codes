import math
print("Permutations of 'n' distinct objects taken 'r' at a time is given by:\nnPr = n!/(n-r)!, where \"!\" denotes the factorial.\n")

try:
    n = int(input("Enter the value of n (n>0): "))
    r = int(input("Enter the value of r (0<=r<=n): "))
    if n<=0 or r<0:
        print("'n' should be greater than 0 and 'r' must be >=0")
    elif r>n:
        print("'r' can't be greater than 'n'")
    else:
        ans = (math.factorial(n))//(math.factorial(n-r))
        print(f"\nPermutation of {n} distinct objects taken {r} at a time is: {ans}")

except Exception as e:
    print(f"ERROR: {e}")
