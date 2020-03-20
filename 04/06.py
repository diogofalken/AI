'''
  Diogo Costa
  13/03/2020

  Description:
    Create a function that gets as params a min value and a max value and prints all the values including them selfs
'''


def min_max(minValue, maxValue):
    for i in range(minValue, maxValue + 1):
        print(i)


min_max(1, 10)
