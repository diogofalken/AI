'''
  Diogo Costa
  2020-04-17

  Description:
    Create a program that uses the numbers 5 to 25 (inclusive) as a key
    and that places the square of the key as the value
'''

dic = {}
for x in range(5, 25):
    dic[x] = x * x

print(dic)