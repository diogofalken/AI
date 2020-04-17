'''
  Diogo Costa
  2020-04-17

  Description:
    Develop a program that takes the inventory of a company. The program allows to select the addition
    or removal of items, as well as the display of existing of items. In the addition operation, they key
    (the name of the product) and the value to be added must be given. If the item already exists, add the
    new value to the existing one. Removing an items will always be based on the key (the product name)
'''

from os import system


def menu():

    while True:
        print(
            'Please select one of the following options:\n\n1 - Insert Items\n2 - Remove items\n3 - List items'
        )
        option = input()
        if (option == '1' or option == '2' or option == '3' or option == '4'):
            break

        return int(option)


def insertItem(dic):
    print('\nPlease give the name of the product ')
    product = input()
    print('\nPlease indicate the value ')
    value = int(input())

    if product not in dic:
        dic.update({product: value})
    else:
        dic[product] += value

    print('Product updated\n')
    return dic


def removeItem(dic):
    print('\nPlease give the name of the product to be removed')
    product = input()

    if product not in dic:
        print(f'{product} was not in the inventory')
    else:
        dic.pop(product)
        print(f'{product} was removed from the inventory')

    return dic


def printItems(dic):
    for k, v in dic.items():
        print(f'Product: {k}\nValue: {v}\n')


if __name__ == "__main__":
    inventory = {}
    while True:
        option = menu()
        if option == 1:
            insertItem(inventory)
        if option == 2:
            removeItem(inventory)
        if option == 3:
            printItems(inventory)
        if option == 4:
            break
