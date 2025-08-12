class complex_number:
    def __init__(self, real, imag):
        self.real = real
        self.imag = imag
    
    def complex_conjugate(self):
        print(f"The complex conjugate of \'{self.real} + {self.imag}i\' is \'{self.real} - {self.imag}i\'")

    def __add__(self, other):
        return complex_number(self.real + other.real, self.imag + other.imag)
    
    def __str__(self):
        return f"{self.real} + {self.imag}i"
    
    def __sub__(self, other):
        return complex_number(self.real - other.real, self.imag - other.imag)
    

s = complex_number(3, 4)
r = complex_number(1, 2)

s.complex_conjugate()
print(f"The sum of {s} and {r} is:", s + r)
print(f"The difference of {s} and {r} is:", s - r)
print(f"The difference of {r} and {s} is:", r - s)
