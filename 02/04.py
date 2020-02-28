'''
  Diogo Costa
  28/02/2020

  Description:
    Make a program with Elif Statements
'''

print("Enter your name:")
name = input()
print("Enter your age:")
age = input()

if name == 'Alice':
    print(f"Hi, {name}.")
elif int(age) < 12:
    print("You are not Alice, kiddo.")
