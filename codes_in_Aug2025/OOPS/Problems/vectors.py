class _2D_vectors:
    def __init__(self, i, j):
        self.i = i
        self.j = j
    
    def vectors(self):
        print(f"2D Vector is: {self.i}i + {self.j}j")

    def magnitude(self):
        print(f"Magnitude of 2D vector is: {(self.i**2 + self.j**2) ** 0.5}")

class _3D_vectors(_2D_vectors):
    def __init__(self, i, j, k):
        super().__init__(i, j)
        self.k = k

    def vectors(self):
        print(f"3D Vector is: {self.i}i + {self.j}j + {self.k}k")
    
    def magnitude(self):
        print(f"Magnitude of 3D vector is: {(self.i**2 + self.j**2 + self.k**2) ** 0.5}")
    
r = _2D_vectors(3, 4)
r.vectors()
r.magnitude()
#-------------
s = _3D_vectors(3, 4, 12)
s.vectors()
s.magnitude()