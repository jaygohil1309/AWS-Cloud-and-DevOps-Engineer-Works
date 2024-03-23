"""

my_package/

    __init__.py
    module1.py
    module2.py

"""
# You can use modules from this package as follow :-

# from my_package import module1

# result = module1.function_from_module1()

"""

In this example, "my_package" is a python package containing modules "module1" and
"module2".

"""

# Example of Packages :-

# Import the entire module

import math

# Use function/variables from the module.....

result = math.sqrt(16)
print(result)

# Import specific function/variable from a module.....

from math import pi
print(pi)