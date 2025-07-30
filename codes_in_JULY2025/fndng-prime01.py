#using the property that squares of prime numbers minus one are divisible by 12
x = int(input("Enter a number to check if it's prime or not: "))
k = (x**2 -1)
#print(f"Calculated value of k: {k}")

if k%12 == 0:
    print(f"{x} is a prime number.")
else:
    print(f"{x} is not a prime number.")