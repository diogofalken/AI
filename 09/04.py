'''
  Diogo Costa
  2020-04-24

  Description:
    Instance Variables
'''


class Scoping:
    def createScopeVariables(self):
        self.value1 = 100
        value2 = 200

    def printLocalVariables(self):
        print(f"Value 2: {value2}")

    def printInstanceVariables(self):
        print(f"Value 1: {self.value1}")


myScope = Scoping()

myScope.printInstanceVariables()

myScope.createScopeVariables()
myScope.printInstanceVariables()  # 100
