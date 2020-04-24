'''
  Diogo Costa
  2020-04-24

  Description:
    Class definition
'''


class MyFirstClass:
    welcome_attribute = "Hello python attributes!"

    def welcome_method(self):
        print("Hello python methods")


# Defining the object instance
myFirstObject = MyFirstClass()

# Calling attributes
print(myFirstObject.welcome_attribute)

# Calling methods
myFirstObject.welcome_method()