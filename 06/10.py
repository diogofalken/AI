'''
  Diogo Costa
  2020-03-27

  Description:
    Get the maximum of a list
'''

numbers_list = [1, 2, 4, 8, 16, 32, 64, 128]

max_number = numbers_list[0]

for i in numbers_list:
    if max_number < i:
        max_number = i

print(max_number)
print(max(numbers_list))