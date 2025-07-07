#importing in python

"""
To import a python module or file you can use the 'import' keyword:
- import math
- math.sqrt(9)

If you want to import selective set of function you can use 'from' keyword:
- from math import sqrt, pi
- sqrt(9)

You can use '*' for all the functions to import:
- from math import *
#It is not recommended because it can lead to confusion in large projects

To use a short name you can use 'as' keyword:
- import math as m
- m.sqrt(9)

or
- from math import sqrt as square_root
- square_root(9)

You check all the functions and variable present in the module you can use dir() :
- import math
- print(dir(math))

You can create your own python file and import it to use the functions.
"""