class Employee:
    def __init__(self, name, salary):
        self.name = name
        self.salary = salary

    def __add__(self, other):
        return Employee(self.name + " & " + other.name, self.salary + other.salary)

    def __sub__(self, other):
        return self.salary - other.salary

    def __str__(self):
        return f"Employee: {self.name}, Salary: ₹{self.salary}"


# Taking user input for employee details
name1 = input("Enter first employee's name: ")
salary1 = int(input("Enter first employee's salary: "))
emp1 = Employee(name1, salary1)

name2 = input("Enter second employee's name: ")
salary2 = int(input("Enter second employee's salary: "))
emp2 = Employee(name2, salary2)

# Using overloaded + operator
combined_emp = emp1 + emp2
print("\nCombined Employee:", combined_emp)

# Using overloaded - operator
salary_diff = emp1 - emp2
print(f"Salary Difference: ₹{abs(salary_diff)}")
