# Coding in style

There are many books and online resources talking about coding style. Here we just want to share some basic principles.

## Naming objects

- Name should be descriptive and self-documenting. 


- Use either `snake_case` or `camelCase` but make it consistent.

## Python Coding Style Tutorial

### Indentation
Use 4 spaces per indentation level. Avoid mixing tabs and spaces. 

### Maximum Line Length
Limit all lines to a maximum of 79 characters.

### Imports
Group imports in the following order: standard library, third-party, local application/library specific. 
### Whitespace
Avoid extraneous whitespace in expressions and statements. 
### Comments
Use comments to explain code. Block comments apply to some or all code that follows them. 

## Python Coding Style Examples

### Naming objects

Names should be descriptive and self-documenting:

```python
# Bad - not descriptive
def f(x):
    return x * 2

# Good - descriptive and self-documenting
def double_number(value):
    return value * 2
```

Use either `snake_case` or `camelCase` but make it consistent:

```python
# snake_case (Python preferred style)
def calculate_average(number_list):
    return sum(number_list) / len(number_list)

# camelCase (less common in Python)
def calculateAverage(numberList):
    return sum(numberList) / len(numberList)
```

### Indentation
Use 4 spaces per indentation level. Avoid mixing tabs and spaces:

```python
# Good indentation
def process_data():
    if condition:
        do_something()
        for item in items:
            process_item()
    
# Bad indentation (mixing spaces)
def process_data():
   if condition:
      do_something()
        for item in items:
         process_item()
```

### Maximum Line Length
Limit all lines to a maximum of 79 characters:

```python
# Bad - too long
result = some_long_function_name(very_long_parameter_name1, very_long_parameter_name2, very_long_parameter_name3)

# Good - split into multiple lines
result = some_long_function_name(
    very_long_parameter_name1,
    very_long_parameter_name2,
    very_long_parameter_name3
)
```

### Imports
Group imports in the following order:
1. Standard library
2. Third-party
3. Local application/library specific

```python
# Good import organization
import os
import sys

import numpy as np
import pandas as pd

from myproject.utils import helper
from myproject.core import main

# Bad import organization
from myproject.utils import helper
import sys
import pandas as pd
from myproject.core import *  # Avoid wildcard imports
import os
```

### Variable Naming and Documentation

```python
# Bad example
def f(x, y):
    a = x + y  # What does 'a' represent?
    return a

# Good example
def calculate_total_price(item_price, tax_rate):
    """Calculate final price including tax.
    
    Args:
        item_price (float): Original price of the item
        tax_rate (float): Tax rate as a decimal (e.g., 0.1 for 10%)
    
    Returns:
        float: Total price including tax
    """
    total_price = item_price * (1 + tax_rate)
    return total_price
```

### Spacing and Operators

```python
# Bad spacing
x=y+z
if x>0:print(x)

# Good spacing
x = y + z
if x > 0:
    print(x)
```

## Tools for coding styles

### Linting

Linting is the process of analyzing your code to check for errors and enforce coding standards. 

Here are some popular linting tools for `Python`:

- [Pylint](https://pypi.org/project/pylint/): it is a static type checker and linting tool for Python.
- [Black](https://pypi.org/project/black/): it is a code formatter that automatically formats your code to adhere to a consistent style.

Please check the VS Code tutorial for python linting [here](https://code.visualstudio.com/docs/python/linting).

The most popular linting tools for `R`:

- [lintr](https://lintr.r-lib.org/articles/lintr.html): it has been integrated into the RStudio and VS Code R extensions.

### Formatting

Formatting is the process of organizing your code to make it more readable.

Please check the VS Code tutorial for python formatting [here](https://code.visualstudio.com/docs/python/formatting).
