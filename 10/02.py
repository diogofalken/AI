'''
  Diogo Costa
  2020-05-08

  Description:
    __dict__ Holds the entity namespace
'''


# Class definition
class NameSpace():
    class_number = 10

    def __init__(self, instance_number):
        self.instance_number = instance_number


# Object creation
new_object = NameSpace(5)

print(new_object.class_number)
print(new_object.instance_number)

print(new_object.__dict__)

print(NameSpace.__dict__)