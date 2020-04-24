'''
  Diogo Costa
  2020-04-24

  Description:
    
'''


class Employee:
    total_employees = 0

    def __init__(self, name, salary):
        print('Constructor is running!\n')
        self.name = name
        print(f"{self.name} is now the valud for self.name instance variable")

        self.salary = salary
        print(
            f"{self.salary} is now the value for self.salary instance variable"
        )

        Employee.total_employees += 1
        print(
            f"The class variable total_employess has now the value of {Employee.total_employees}"
        )

    def totalNumberOfEmployees(self):
        print(f"Total number of employees: {self.total_employees}")

    def showDetail(self):
        print(f"\nName: {self.name}\nSalary: {self.salary}")


# Object creation
employee1 = Employee('Anne', 5000)