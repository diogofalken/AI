'''
  Diogo Costa
  28/02/2020

  Description:
    - Blocks of code
    Lines of Python code can be grouped together in blocks. You can tell when a block
    begins and ends from the indenteation of the lines of code
    - Rules
      - Blocks begin when the indentation increases.
      - Blocks can contain other blocks
      - Blocks end when the indentation decreases to zero or to a containing block's indentation.  
'''

name = 'Filipe'
password = 'root'

if name == 'Filipe':
    print(f"Hello {name}")
    if password == 'root':
        print('Access granted.')
    else:
        print('Wrong password.')
