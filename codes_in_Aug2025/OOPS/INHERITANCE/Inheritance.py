class employee:
    company = "Microsoft"
    language = "Python"

    def __init__(self, name):
        self.name = name

    def info(self):
        print(f"The name of the employee is {self.name}. He is in the company: {self.company}, He uses the language: {self.language}")

class programmer(employee): # Inherits from employee
    company = "Google"  # Overrides class variable
    language = "Java"

bob = employee("Bob")
bob.info()

alice = programmer("Alice")
alice.info()
