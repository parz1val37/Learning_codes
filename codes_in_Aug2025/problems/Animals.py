class animals:
    pass

class pets(animals):
    pass

class dog(pets):
    @staticmethod
    def bark():
        print("Woof! Woof!")

tom = dog()
tom.bark()  