# 0x01. Python - Async
- Python
- Back-end

This project contains tasks for learning to use asynchronous code in Python 3.

## Requirements

- A README.md file, at the root of the folder of the project, is mandatory
- Allowed editors: vi, vim, emacs
- All your files will be interpreted/compiled on Ubuntu 18.04 LTS using python3 (version 3.7)
- All your files should end with a new line
All your files must be executable
- The length of your files will be tested using wc
The first line of all your files should be exactly #!/usr/bin/env python3
Your code should use the pycodestyle style (version 2.5.x)
- All your functions and coroutines must be type-annotated.
All your modules should have a documentation (python3 -c 'print(__import__("my_module").__doc__)')
- All your functions should have a documentation (python3 -c 'print(__import__("my_module").my_function.__doc__)'

A documentation is not a simple word, it’s a real sentence explaining what’s the purpose of the module, class or method (the length of it will be verified)

## Tasks To Complete

+ [x] 0. **The basics of async**<br/>[0-basic_async_syntax.py](0-basic_async_syntax.py) contains an asynchronous coroutine that takes in an integer argument (`max_delay`, with a default value of 10) named `wait_random` that waits for a random delay between 0 and `max_delay` (included and float value) seconds and eventually returns it. The `random` module should be used.

+ [x] 1. **Let's execute multiple coroutines at the same time with async**<br/>[1-concurrent_coroutines.py](1-concurrent_coroutines.py) contains a script that meets the following requirements:
  + Import `wait_random` from the previous python file that you’ve written and write an async routine called `wait_n` that takes in 2 int arguments (in this order): `n` and `max_delay`. You will spawn wait_random n times with the specified `max_delay`.
  + `wait_n` should return the list of all the delays (float values). The list of the delays should be in ascending order without using `sort()` because of concurrency.

+ [x] 2. **Measure the runtime**<br/>[2-measure_runtime.py](2-measure_runtime.py) contains a script that meets the following requirements:
  + From the previous file, import `wait_n` into [2-measure_runtime.py](2-measure_runtime.py).
  + Create a `measure_time` function with integers `n` and `max_delay` as arguments that measures the total execution time for `wait_n(n, max_delay)`, and returns `total_time / n`. Your function should return a float.
  + Use the `time` module to measure an approximate elapsed time.

+ [x] 3. **Tasks**<br/>[3-tasks.py](3-tasks.py) contains a script that meets the following requirements:
  + Import `wait_random` from [0-basic_async_syntax](0-basic_async_syntax).
  + Write a function (do not create an async function, use the regular function syntax to do this) `task_wait_random` that takes an integer `max_delay` and returns a `asyncio.Task`.

+ [x] 4. **Tasks**<br/>[4-tasks.py](4-tasks.py) contains a script that meets the following requirements:
  + Take the code from `wait_n` and alter it into a new function `task_wait_n`. The code is nearly identical to `wait_n` except `task_wait_random` is being called.
