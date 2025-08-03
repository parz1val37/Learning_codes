#method 01: using function and  loop

def sum_ntrl():
    n = int(input("Enter a natural number: "))
    sum = 0
    for i in range(1, n + 1):
        sum += i
    print(f"The sum of natural numbers from 1 to {n} is: {sum}")
sum_ntrl()

#method 02: by a formula of sum of n natural numbers

def sum_ntrl_formula():
    n = int(input("Enter a natural number: "))
    sum = (n * (n + 1))/ 2
    print(f"The sum of natural numbers from 1 to {n} is: {sum}")
sum_ntrl_formula()

#method 03: using recursion

def sum_ntrl_recursive(n):
    if n == 0:
        return 0
    else:
        return n + sum_ntrl_recursive(n - 1)
n = int(input("Enter a natural number: "))
print(f"The sum of natural numbers from 1 to {n} is: {sum_ntrl_recursive(n)}")