'''
  Diogo Costa
  28/02/2020

  Description:
    Make a program with more Elif Statements
'''

print("Enter your name:")
name = input()
print("Enter your age:")
age = input()

if name == 'Alice':
    print(f"Hi, {name}.")
elif int(age) < 12:
    print("You are not Alice, kiddo.")
elif int(age) > 2000:
    print(f"Unlike you {name}, Alice is not an undead, immortal vampire.")
elif int(age) > 100:
    print("You are not Alice, grannie.")
