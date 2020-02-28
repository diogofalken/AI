'''
  Diogo Costa
  28/02/2020

  Description:
    Make a program with Continue Statement
'''

from getpass import getpass

while True:
    print("Please enter your name:")
    name = input()

    if name != 'Joe':
        continue
    else:
        print("Hello, Joe Mama. What is the password? (It is a fish)")
        password = getpass()

        if password == 'swordfish':
            break

print(f"Access granted, {name}.")
