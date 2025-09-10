def Fibonacci(n):
    sequence = [0,1]
    i = 0
    while i<(n-2):
        sequence.append(sequence[i] + sequence [i+1])
    i += 1
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
        print(f"Fibonacci series of {n} digit is:\n{Fibonacci(n)}")
except Exception as e:
    print(f"ERROR: {e}")