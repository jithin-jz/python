# 🔹 2. Employee Salary

# Create a class Employee with attributes name, salary.

# Add a method give_raise(amount) that increases the salary.

# Create two employees and give one of them a raise.

class Employee:
    def __init__(self, name: str, salary: float):
        self.name = name
        self.salary = salary
        
    def give_raise(self,amount:float):
        self.salary +=amount

    def __str__(self) -> str:
        return f"{self.name} has a salary of {self.salary}"

em1 = Employee("Jithin", 44000)
em2 = Employee("Anand", 45000)

em1.give_raise(1500)
em2.give_raise(500)

print(em1)
print(em2)
