class employee:
    salary = 1000
    language = "Python"
    age = 30

    def info(self):
        print("Name:", self.name)
        print("Salary:", self.salary)
        print("Language:", self.language)
        print("Age:", self.age)

    def __init__(self, name, salary, language, age):
        self.name = name
        self.salary = salary
        self.language = language
        self.age = age

Bob = employee("Bob", 2000000, "Java", 25)
print(Bob.salary)
Bob.info()