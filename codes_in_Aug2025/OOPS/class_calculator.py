class calculator:
    def square(self,x):
        print(f"The square of {x} is: {x * x}")
    def cube(self,x):
        print(f"The cube of {x} is: {x * x * x}")
    def sqrt(self,x):
        print(f"The square root of {x} is: {x ** 0.5}")

calc = calculator()
calc.square(4)
calc.sqrt(36)
# calc.sqrt(15)
calc.cube(2)
