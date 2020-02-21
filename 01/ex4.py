'''
  Diogo Costa
  21/02/2020

  Description:
    Develop a program that asks the user for their name, year of birth, street and postal code. The program should welcome
    the user and return their age. You must also provide the full address (street and postal code) as well as indicate
    the number of characters used
'''
print("What is your name?")
name = input()

print("What year were you born?")
birth_year = input()

print("What is your street")
street = input()

print("What is your postal code?")
postal_code = input()

final_string = f"Hey {name} you are {2020 - int(birth_year)} and you currently live in {street + ',' + postal_code}."

print(f"{final_string} This sentence as {len(final_string)} chars.")
