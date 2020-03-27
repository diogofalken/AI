'''
  Diogo Costa
  2020-03-27

  Description:
    Lists - .remove()
'''

fruits = ["apples", 'pears', 'tomatos', 'pears','tangerines']

# removing the first matching value
fruits.remove("apples")
print(fruits)

# removing a non existant element
fruits.remove("apples")  # Will give an error
print(fruits)

# removing a duplicate element
fruits.remove('pears') # Will remove the first appear
print(fruits)