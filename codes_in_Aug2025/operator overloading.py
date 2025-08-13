class number:
    def __init__(self, n):
        self.n = n

    def __add__(self, num):     #dunder/magic method for addition
        return self.n + num.n
    
x = number(10)
y = number(20)
result = x + y
print(result)