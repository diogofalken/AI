'''
  Diogo Costa
  2020-03-27

  Description:
    Sum of all elements of a list
'''

numbers_list = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

total = 0

for i in numbers_list:
    total += i

print(total)
print(sum(numbers_list))