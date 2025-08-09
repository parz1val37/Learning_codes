class employee:
    salary = 12345678
    language = "Python"
    age = 30

    def info(self):
        print("Salary:", self.salary)
        print("Language:", self.language)
        print("Age:", self.age) 
    
    @staticmethod
    def greet():
        print("Hello, I am an employee.")

Bob = employee()
Bob.language = "Java"
Bob.age = 35
Bob.greet()
Bob.info()