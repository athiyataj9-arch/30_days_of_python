# ==========================================
# DAY 26: OOP INHERITANCE & POLYMORPHISM 🧬
# ==========================================

# 1. PARENT CLASS (Base Class)
class Employee:
    def __init__(self, name, salary):
        self.name = name
        self.salary = salary

    def get_details(self):
        return f"Employee: {self.name} | Salary: ${self.salary:,}"

# 2. CHILD CLASS (Subclass)
# This class inherits everything from Employee
class Developer(Employee):
    def __init__(self, name, salary, language):
        # 'super()' calls the constructor of the Parent class
        super().__init__(name, salary)
        self.language = language

    # Overriding the Parent method (Polymorphism)
    def get_details(self):
        return f"Developer: {self.name} | Language: {self.language} | Salary: ${self.salary:,}"

# 3. USING THE CLASSES
emp1 = Employee("John Doe", 50000)
dev1 = Developer("Athiya", 95000, "Python")

print(emp1.get_details())
print(dev1.get_details())