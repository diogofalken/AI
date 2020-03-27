'''
  Diogo Costa
  2020-03-27

  Description:
    Lists using Deep Copy (new in JAVA)
'''

numbers = [[1, 2], [5, 6], [9, 10]]

# Using deep copy creates a complete new object with the values of the nested objects
import copy
new_list = copy.deepcopy(numbers)
print(numbers)
print(new_list)

# appending new values to the old (or new list)
numbers.append([13, 14])
print(numbers)
print(new_list)

# changing existing values in a nested list
numbers[0][1] = 1000
print(numbers)
print(new_list) 