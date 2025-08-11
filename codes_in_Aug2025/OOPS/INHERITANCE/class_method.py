class testing:
    x = 3
    y = 21
    @classmethod
    def show(cls):
        print("The class attribute of x is:", cls.x)

    def show_y(self):
        print("The instance attribute of y is:", self.y)

num = testing() 
num.x = 5  # This will not change the class attribute x, but create an instance attribute x
num.y = 37

num.show()  # This will call the class method and print the class attribute x
num.show_y()  # This will call the instance method and print the instance attribute y
testing.show()  # This will also call the class method and print the class attribute x