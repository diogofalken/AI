'''
  Diogo Costa
  2020-05-08

  Description:
    __name__
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


# Print class name
print(Car.__name__)

# Car creation
car1 = Car('Toyota', 'Corola', 'Blue')

# print(car1.__name__) # Error
