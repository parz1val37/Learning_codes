class employee:
    company = "Microsoft"

    def __init__(self, name):
        self.name = name

    def info(self):
        print(f"The name of the employee is {self.name}. He is in the company: {self.company}.")

class coder:
    language = "Python"

    def showlanguage(self):
        print(f"The language used is {self.language}.")

class programmer(employee, coder): # Inherits from employee and coder ------ Derived class
    company = "Google"  # Overrides class variables
    language = "Java"

bob = employee("Bob")
bob.info()

alice = programmer("Alice")
alice.info()
alice.showlanguage()