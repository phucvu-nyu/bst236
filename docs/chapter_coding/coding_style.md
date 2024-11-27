# Coding in style

There are many books and online resources talking about coding style. Here we just want to share some basic principles.

## Naming objects

- Name should be descriptive and self-documenting.
  ```python
  # Function for falling objects based on Newton's equation
  # This is a bad example of not self-documenting function
  def func(y):
      # z is gravitational force
      z = 9.81
      # y is time in seconds
      y = 5
      # x is displacement
      x = 1/2 * z * y**2
      return x
  # This is a self-documenting function
  def compute_displacement(time_in_seconds):
      gravitational_force = 9.81
      displacement = 1/2 * gravitational_force * time_in_seconds**2
      return displacement
  # Even better to set constants as function variables
  def compute_displacement(time_in_seconds, 
                           gravitational_force=9.81,
                           ):
      displacement = 1/2 * gravitational_force * time_in_seconds**2
      return displacement
  ```

- Use either `snake_case` or `camelCase` but make it consistent.

## Python Coding Style Tutorial

### Indentation
Use 4 spaces per indentation level. Avoid mixing tabs and spaces.

```python
def example_function():
    if True:
        print("Use 4 spaces for indentation")
```

### Maximum Line Length
Limit all lines to a maximum of 79 characters.

```python
# This is a long comment that should be wrapped to fit within the 79 character limit.
```

### Imports
Group imports in the following order: standard library, third-party, local application/library specific.

```python
import os
import sys

import numpy as np

from mymodule import myfunction
```

### Whitespace
Avoid extraneous whitespace in expressions and statements.

```python
# Correct
spam(ham[1], {eggs: 2})

# Wrong
spam( ham[ 1 ], { eggs: 2 } )
```

### Comments
Use comments to explain code. Block comments apply to some or all code that follows them.

```python
# This function calculates the displacement of a falling object.
def compute_displacement(time_in_seconds, gravitational_force=9.81):
    displacement = 1/2 * gravitational_force * time_in_seconds**2
    return displacement
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
