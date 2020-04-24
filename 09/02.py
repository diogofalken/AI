'''
  Diogo Costa
  2020-04-24

  Description:
    Class - scoping
'''


class Employee:
    total_employees = 0

    def __init__(self, name, salary):
        self.name = name
        self.salary = salary
        Employee.total_employees += 1

    def totalNumberOfEmployees(self):
        print(f"Total number of employees: {self.total_employees}")

    def showDetail(self):
        print(f"\nName: {self.name}\nSalary: {self.salary}")


# Object creation
employee1 = Employee('Peter', 1500)

# Object usage
employee1.totalNumberOfEmployees()
employee1.showDetail()

# Object creation
employee2 = Employee('Ben', 2000)

# Object usage
employee2.totalNumberOfEmployees()
employee2.showDetail()

employee1.total_employees = 1000  # Creates a variable in employee1 namespace

employee1.totalNumberOfEmployees()
employee2.totalNumberOfEmployees()