#Sum of N Natural Numbers using While Loop
n = int(input("Enter a positive integer: "))
i = 1
sum_n = 0
while i <= n:
    sum_n += i
    i += 1

print(f"The sum of the first {n} natural numbers is: {sum_n}")