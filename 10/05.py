'''
  Diogo Costa
  2020-05-08

  Description:
    Write a program, using a py class, named Rectangle, constructed by a given length and width
    The class must provide a method to compute the area and a method to compute the perimeter
    The class and methods docstrings must be provided
    The class must also provide the total number of rectangles created
'''


class Rectangle:
    '''This class holds all the info from a rectangle.'''

    nRectangles = 0

    def __init__(self, _length, _width):
        '''Initializes the rectangle with a length and width.'''
        self.length = _length
        self.width = _width
        Rectangle.nRectangles += 1

    def area(self):
        '''Computes the area of the rectangle.'''
        area = self.length * self.width

        print(f"The area of the rectangle is {area}")

    def perimeter(self):
        '''Computes the perimeter of the rectangle.'''
        perimeter = 2 * (self.length + self.length)

        print(f"The area of the rectangle is {perimeter}")

    def total(self):
        '''This method prints the total number of rectangles'''
        print(f"Total number of rectangles is {Rectangle.nRectangles}")


rec1 = Rectangle(10, 14)

print("----- Rectangle 1 -----")
rec1.area()
rec1.perimeter()
rec1.total()

rec2 = Rectangle(4, 10)

print("----- Rectangle 2 -----")
rec2.area()
rec2.perimeter()
rec2.total()

print("----- Documentation -----")
print(Rectangle.__doc__)
print(rec1.area.__doc__)
print(rec1.perimeter.__doc__)