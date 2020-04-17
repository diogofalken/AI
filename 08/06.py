'''
  Diogo Costa
  2020-04-17

  Description:
    Write a function that returns a new dictionary from dictionaries passed as parameters
'''

car = {'brand': 'toyota', 'color': 'black', 'plate': '11-TT-23'}
car1 = {'x': 'seat', 'y': 'black', 'z': '11-TT-23'}


def Merge(dict1, dict2):
    output = dict1.copy()
    output.update(dict2)
    return output


print(Merge(car, car1))
