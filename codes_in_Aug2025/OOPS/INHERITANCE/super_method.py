class employee:
    company = "works in Microsoft"

    def __init__(self):
        print("Employee class constructor.")

class coder(employee):  # Inherits from employee 
    language = "Python"
    company = "Works in Google"  # Overriding the company attribute
    def __init__(self):
        print("Coder class constructor.")

    def showlanguage(self):
        print(f"The language used is {self.language}.")

class manager(coder):  # Inherits from both coder and employee
    name = "Trevor" 

    def __init__(self):
        super().__init__()
        print("Manager class constructor.")

    def showname(self):
        print(f"The name of the manager is {self.name}.")

trevor = manager() 