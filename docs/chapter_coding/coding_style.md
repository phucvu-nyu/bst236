# Coding in style

There are many books and online resources talking about coding style. Here we just want to share some basic principles.

## Naming objects

- Name should be descriptive and self-documenting. See examples in [python_style.py](../codes/python/chapter_coding/python_style.py).

- Use either `snake_case` or `camelCase` but make it consistent.

## Python Coding Style Tutorial

### Indentation
Use 4 spaces per indentation level. Avoid mixing tabs and spaces. Examples can be found in [python_style.py](../codes/python/chapter_coding/python_style.py).

### Maximum Line Length
Limit all lines to a maximum of 79 characters.

### Imports
Group imports in the following order: standard library, third-party, local application/library specific. See examples in [python_style.py](../codes/python/chapter_coding/python_style.py).

### Whitespace
Avoid extraneous whitespace in expressions and statements. Examples of correct and incorrect usage can be found in [python_style.py](../codes/python/chapter_coding/python_style.py).

### Comments
Use comments to explain code. Block comments apply to some or all code that follows them. See examples of good and bad commenting practices in [python_style.py](../codes/python/chapter_coding/python_style.py).

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
