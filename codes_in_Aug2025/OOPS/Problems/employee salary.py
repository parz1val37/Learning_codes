class employee:
    salary = 10000
    increment = 37

    @property
    def salary_with_increment(self):
        return f"Salary after increment is: {self.salary + (self.salary * self.increment / 100)}"
    
    @salary_with_increment.setter
    def salary_with_increment(self, new_salary):
        self.increment = ((new_salary/self.salary) - 1) * 100
    
y = employee()
# print(y.salary_with_increment)
# print(y.increment)
print(f"Salary is: {y.salary}")
y.salary_with_increment = 30000 
print(f"Increment is: {y.increment}")
print(y.salary_with_increment)