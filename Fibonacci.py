def fibonacci(n):
    sequence = [0,1]

    for _ in range(n-2):
        sequence.append(sequence[-2] + sequence [-1])
    return sequence

try:
    n = int(input("Upto how many digits you want the Fibonacci sequence: "))
    if n<=0:
        print("Enter a natural number.")
    if n==1:
        print("Fibonacci series of 1 digit is [0]")
    if n==2:
        print("Fibonacci series of 2 digit is [0,1]")
    if n>2:
        print(f"Fibonacci series of {n} digit is:\n{fibonacci(n)}")
except Exception as e:
    print(f"ERROR: {e}")
