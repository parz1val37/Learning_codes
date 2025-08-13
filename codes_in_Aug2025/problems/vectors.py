class _2D_vectors:
    def __init__(self, i, j):
        self.i = i
        self.j = j
    
    def vectors(self):
        print(f"2D Vector is: {self.i}i + {self.j}j")

    def magnitude(self):
        print(f"Magnitude of 2D vector is: {(self.i**2 + self.j**2) ** 0.5}")
    
    def __str__(self):
        return f"{self.i}i + {self.j}j"

    def __add__(self, other):
        return _2D_vectors(self.i + other.i, self.j + other.j)

    def dot_product(self, other):
        return self.i * other.i + self.j * other.j

class _3D_vectors(_2D_vectors):
    def __init__(self, i, j, k):
        super().__init__(i, j)
        self.k = k

    def vectors(self):
        print(f"3D Vector is: {self.i}i + {self.j}j + {self.k}k")
    
    def magnitude(self):
        print(f"Magnitude of 3D vector is: {(self.i**2 + self.j**2 + self.k**2) ** 0.5}")
    
    def __str__(self):
        return f"{self.i}i + {self.j}j + {self.k}k"
    
    def dot_product(self, other):
        return self.i * other.i + self.j * other.j + self.k * other.k
    
    def __add__(self, other):
        return _3D_vectors(self.i + other.i, self.j + other.j, self.k + other.k)

r = _2D_vectors(3, 4)
r.vectors()
r.magnitude()
k = _2D_vectors(1, 2)
print(f"The sum of {r} and {k} is:", r + k)
print(f"The dot product of {r} and {k} is:", r.dot_product(k))

#-------------
s = _3D_vectors(3, 4, 12)
s.vectors()
s.magnitude()
p = _3D_vectors(1, 2, 5)
print(f"The sum of {s} and {p} is:", s + p)
print(f"The dot product of {s} and {p} is:", s.dot_product(p))
print(f"The dot product of {r} and {s} is:", r.dot_product(s))