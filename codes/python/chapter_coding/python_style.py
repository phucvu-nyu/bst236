# Examples of Python coding style - both good and bad practices

# Example 1: Function Naming and Documentation
# Bad example - not self-documenting
def func(y):
    # z is gravitational force
    z = 9.81
    # y is time in seconds
    y = 5
    # x is displacement
    x = 1/2 * z * y**2
    return x

# Good example - self-documenting
def compute_displacement(time_in_seconds):
    gravitational_force = 9.81
    displacement = 1/2 * gravitational_force * time_in_seconds**2
    return displacement

# Even better - with parameters
def compute_displacement(time_in_seconds, 
                       gravitational_force=9.81):
    displacement = 1/2 * gravitational_force * time_in_seconds**2
    return displacement

# Example 2: Indentation
def example_function():
    if True:
        print("Use 4 spaces for indentation")

# Example 3: Imports
import os
import sys

import numpy as np

from mymodule import myfunction

# Example 4: Whitespace in Expressions
# Correct
spam(ham[1], {eggs: 2})
# Wrong
spam( ham[ 1 ], { eggs: 2 } )

# Example 5: Comments and Documentation
# This function calculates the displacement of a falling object.
def compute_displacement(time_in_seconds, gravitational_force=9.81):
    displacement = 1/2 * gravitational_force * time_in_seconds**2
    return displacement

# Bad Python Code Example - How NOT to Write Python
def calculate_stuff(a,b,c):   # pylint: disable=invalid-name
    # Single letter variable names are not descriptive
    # No space after comma in parameters (PEP 8 violation)
    # Missing function docstring
    
    x=a+b # No spaces around operators
    
    if x>10: # No spaces around comparison operator
        # Using global variable
        global result 
        result=x+c
    
    # Inconsistent return statements (sometimes returns None implicitly)
    if result>20:
        return result

# Global variable defined outside of function
result = 0

class badclass:  # Class name doesn't use CapWords convention
    # Missing class docstring
    
    def __init__(self):
        # Using single letter variable name
        self.x=0  # No space around operator
    
    def Do_Something(self):  # Method name not in lowercase with underscores
        # Using magic number without explanation
        self.x+=42
        
        # Too many blank lines (Pylint prefers max 2)


        # Line too long - Pylint typically warns when lines exceed 100 characters
        return self.x

# No space around operator and poor variable name
i=0

# Using wildcard imports
from math import *

# Unused import
import sys

# Multiple statements on one line
i+=1; print(i)
