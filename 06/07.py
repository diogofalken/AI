'''
  Diogo Costa
  2020-03-27

  Description:
    Passing values copy
'''

numbers = [[1, 2], [5, 6], [9, 10]]

# Using copy creates a new object with the reference of nested objects
import copy
new_list = copy.copy(numbers)
print(new_list)
print(numbers)

# appending new values to the old (or new list)
numbers.append([13, 14])

print(new_list)
print(numbers)

# changing existing values in a nested list
numbers[0][1] = 1000
print(numbers)
print(new_list)