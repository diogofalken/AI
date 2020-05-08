'''
  Diogo Costa
  2020-05-08

  Description:
    __doc__ Provides the docstring documentation
'''


class Car:
    '''This class allow the characterization of cars.'''
    number_of_cars = 0

    def __init__(self, brand, model, color):
        '''This is the object constructor.'''
        self.brand = brand
        self.model = model
        self.color = color
        Car.number_of_cars += 1

    def print_details(self):
        '''This fucntions prints the details of a car.'''
        print('Car')
        print(f'Brand: {self.brand}')
        print(f'Model: {self.model}')
        print(f'Color: {self.color}')

    def total_number_of_cars(self):
        '''This fucntion prints the total number of cars.'''
        print(f"Total number of cars: {str(Car.number_of_cars)}")


# Car creation
car1 = Car('Toyota', 'Corola', 'Blue')

# Printing class documentation
print(Car.__doc__)

# Printing object documentation
print(car1.__doc__)

# Printing the __init__ documentation of the class
print(Car.__init__.__doc__)

# Printing the __init__ documentation of the object
print(car1.__init__.__doc__)

# Printing the print_details documentation of the object
print(car1.print_details.__doc__)