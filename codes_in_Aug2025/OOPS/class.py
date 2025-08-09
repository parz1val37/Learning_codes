class Employee:
    age = 19
    language = "Python"        #class attribute
    salary = 1200000

max = Employee()
max.name = "Max"    #object attribute or instance attribute
max.language = "Java"  #overriding class attribute
# max.name = "Maxwell"  #overriding object attribute
print(f"{max.name}\n{max.language}\n{max.age}")

#----instance attributes can override class attributes
