def division(divideBy):
    try:
        return 10 / divideBy
    except ZeroDivisionError:
        print('Error: Invalid argument')


try:
    print(division(10))
    print(division(5))
    print(division(0))
    print(division(1))
except ZeroDivisionError:
    print('Error: Invalid argument')
