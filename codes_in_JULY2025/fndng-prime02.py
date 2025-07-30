x = int(input("Enter a number to check for prime: "))
        
for i in range(2,x):
    if x % i == 0:
        print(f"{x} is not a prime number.")
        break
else:
    print(f"{x} is a prime number.")
        