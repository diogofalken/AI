'''
  Diogo Costa
  2020-05-08

  Description:
    Delete class atributtes
'''


class Car:
    number_of_cars = 0

    def __init__(self, brand, model, color):
        self.brand = brand
        self.model = model
        self.color = color
        Car.number_of_cars += 1

    def print_details(self):
        print('Car')
        print(f'Brand: {self.brand}')
        print(f'Model: {self.model}')
        print(f'Color: {self.color}')

    def total_number_of_cars(self):
        print(f"Total number of cars: {str(Car.number_of_cars)}")


car1 = Car("Toyota", "Yaris", "Branco")

print(car1.total_number_of_cars)
delattr(car1.total_number_of_cars)
print(car1.total_number_of_cars)
