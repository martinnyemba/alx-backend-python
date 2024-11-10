# 0x00. Python - Variable Annotations

## 📖 Overview

This project focuses on Python Variable Annotations, where you'll learn to use Python's type hinting features to improve code readability, error checking, and documentation. We will explore how to specify function signatures, annotate variables, leverage Python's dynamic typing, and validate our code using tools like mypy.

## 🛠️ Key Concepts:

Type Annotations in Python 3

Duck Typing

Static Type Checking with mypy


## 📚 Resources

Make sure to check out the following resources to get the most out of this project:

Python 3 Typing Documentation

MyPy Cheat Sheet



---

## 🎯 Learning Objectives

By the end of this project, you should be able to:

Understand and apply type annotations in Python.

Use type hints to specify function signatures and variable types.

Implement the concept of Duck Typing.

Validate Python code using mypy for type checking.



---

## ⚙️ Requirements

Python version: Python 3.7

OS: Ubuntu 18.04 LTS

Code style: Pycodestyle (version 2.5)

Editors: vi, vim, emacs

All files should be executable.

Use #!/usr/bin/env python3 as the first line in your Python scripts.

Each file must end with a new line.

Include documentation for all modules, classes, and functions.



---

## 📂 Project Structure
```
0x00-python_variable_annotations/
├── 0-add.py
├── 1-concat.py
├── 2-floor.py
├── 3-to_str.py
├── 4-define_variables.py
├── 5-sum_list.py
├── 6-sum_mixed_list.py
├── 7-to_kv.py
├── 8-make_multiplier.py
├── 9-element_length.py
└── README.md
```

---

## 📝 Tasks

0. Basic Annotations - Add

Write a function add that takes two floats and returns their sum.

def add(a: float, b: float) -> float:
    return a + b

File: 0-add.py

1. Basic Annotations - Concat

Write a function concat that takes two strings and returns their concatenation.

def concat(str1: str, str2: str) -> str:
    return str1 + str2

File: 1-concat.py

2. Basic Annotations - Floor

Write a function floor that takes a float and returns its floor value.

import math

def floor(n: float) -> int:
    return math.floor(n)

File: 2-floor.py

3. Basic Annotations - To String

Write a function to_str that converts a float to its string representation.

def to_str(n: float) -> str:
    return str(n)

File: 3-to_str.py

4. Define Variables

Define variables with specific types.

a: int = 1
pi: float = 3.14
i_understand_annotations: bool = True
school: str = "Holberton"

File: 4-define_variables.py

5. Complex Types - List of Floats

Write a function sum_list that takes a list of floats and returns their sum.

from typing import List

def sum_list(input_list: List[float]) -> float:
    return sum(input_list)

File: 5-sum_list.py

6. Complex Types - Mixed List

Write a function sum_mixed_list that handles lists with both integers and floats.

from typing import List, Union

def sum_mixed_list(mxd_lst: List[Union[int, float]]) -> float:
    return sum(mxd_lst)

File: 6-sum_mixed_list.py

7. Complex Types - Tuple

Write a function to_kv that takes a string and an int/float and returns a tuple.

from typing import Union, Tuple

def to_kv(k: str, v: Union[int, float]) -> Tuple[str, float]:
    return (k, v ** 2)

File: 7-to_kv.py

8. Complex Types - Function as Return Type

Write a function make_multiplier that returns a function to multiply a float by a given multiplier.

from typing import Callable

def make_multiplier(multiplier: float) -> Callable[[float], float]:
    return lambda x: x * multiplier

File: 8-make_multiplier.py

9. Duck Typing - Iterables

Annotate a function's parameters and return values for handling iterables.

from typing import Iterable, Sequence, List, Tuple

def element_length(lst: Iterable[Sequence]) -> List[Tuple[Sequence, int]]:
    return [(i, len(i)) for i in lst]

File: 9-element_length.py


---

## 🧪 Testing

To test your implementations, use the provided main files and run:

./0-main.py
./1-main.py
...
./9-main.py

Ensure all type annotations are correctly defined by checking with mypy:

mypy 0-add.py
mypy 1-concat.py
...
mypy 9-element_length.py


---

## 📜 License

This project is © 2024 ALX, all rights reserved.

Happy Coding! 😊
