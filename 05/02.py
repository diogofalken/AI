'''
  Diogo Costa
  2020-03-20

  Description:
    Slicing
'''

# list definition
pencil_case = ["pen", 'pencil', 'sharpener', 'scissors']

# slicing elements 1 and 2
print(pencil_case[1:3])

# slicing elements 1,2 and 3
print(pencil_case[1:4])

# slicing elements 0,1,2 and 3
print(pencil_case[0:4])

# out of range slicing are handled gracefully
print(pencil_case[0:10])

# from the last but one till the end
print(pencil_case[-1:4])