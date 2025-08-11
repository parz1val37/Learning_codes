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

class manager(coder):
    name = "Rani"  # Inherits from coder
    def __init__(self):
        print("Manager class constructor.")
    def showname(self):
        print(f"The name of the manager is {self.name}.")

karan = employee() # This will call the employee constructor
print(karan.company)
#---------------------
rohit = coder()
print(rohit.company)
rohit.showlanguage()
#-----------------------
rani = manager()
print(rani.company)
rani.showlanguage()
rani.showname() # This will call the showname method of manager

#----------Use of super() to call parent class methods----------
