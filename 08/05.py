'''
  Diogo Costa
  2020-04-17

  Description:
    Write a function that receives a dictionary and key. The function must
    check if the key is present in the dictionary. If so, return a new 
    dictionary with the key and its value. If not, return an empty dictionary
'''

car = {'brand': 'toyota', 'color': 'black', 'plate': '11-TT-23'}


def checkKey(dic, key):
    ouput = {}
    ouput[key] = car.get(key)

    if ouput[key] == None:
        ouput = {}

    return ouput


print(checkKey(car, 'brand'))
print(checkKey(car, 'teste'))
