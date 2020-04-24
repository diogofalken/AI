'''
  Diogo Costa
  2020-04-24

  Description:
    Create a class called "Car", which has the brand, model and color of the vehicle as attributes. The class must also have a function
    that allows printing all the characteristics of the vehicle. The class should allow printing the total number of existing vehicles

    Create two objects to characterize two different vehicles and call the object method to print all their characteristics. Call also 
    the other method to print the local number of cars
'''


class Car:
    totalCars = 0

    def __init__(self, brand, model, color):
        self.brand = brand
        self.model = model
        self.color = color

        Car.totalCars += 1

    def printCarInfo(self):
        print("---- Car info ----")
        print(f"Brand: {self.brand}\nModel: {self.model}\nColor: {self.color}")

    def printTotalNumberOfCars(self):
        print(f"Total number of cars is {self.totalCars}")


car1 = Car("Toyota", "Yaris", "White")
car2 = Car("Mercedes", "A200", "Mate Black")

car1.printCarInfo()
car2.printCarInfo()

car1.printTotalNumberOfCars()
car2.printTotalNumberOfCars()