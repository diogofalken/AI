'''
  Diogo Costa
  2020-03-27

  Description:
    Remove all instances in a list
'''

fruits = ["apples", 'pears', 'tomatos', 'pears', 'tangerines']

for x in fruits:
    if x == 'pears':
        fruits.remove('pears')

print(fruits)