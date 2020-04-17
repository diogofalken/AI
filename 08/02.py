'''
  Diogo Costa
  2020-04-17

  Description:
    Dictionaries Pop
'''

car = {'brand': 'toyota', 'color': 'black', 'plate': '11-TT-23'}
print(car)
returnedValue = car.pop("brand")
print(returnedValue)
print(car)

# returnedValue = car.pop('year')
# print(returnedValue)

returnedValue = car.pop('year', 1900)
print(returnedValue)