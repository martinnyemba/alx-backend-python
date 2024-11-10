# 0x02. Python - Async Comprehension

## Table of Contents
- [Description](#description)
- [Learning Objectives](#learning-objectives)
- [Requirements](#requirements)
- [Project Structure](#project-structure)
- [Tasks](#tasks)
  - [Task 0: Async Generator](#task-0-async-generator)
  - [Task 1: Async Comprehensions](#task-1-async-comprehensions)
  - [Task 2: Run Time for Four Parallel Comprehensions](#task-2-run-time-for-four-parallel-comprehensions)
- [Usage](#usage)
- [Examples](#examples)
- [Resources](#resources)
- [Author](#author)

## Description
This project focuses on asynchronous programming in Python, specifically using asynchronous comprehensions and generators. It covers how to use `async` and `await` keywords to write asynchronous code, which is useful for I/O-bound operations to improve performance and responsiveness in applications.

## Learning Objectives
By the end of this project, you will be able to:
- Write an asynchronous generator in Python.
- Use async comprehensions to collect data from asynchronous generators.
- Type-annotate generators and coroutines for better code readability and error checking.

## Requirements
- Python 3.7
- Ubuntu 18.04 LTS
- All code should follow the **pycodestyle** (version 2.5.x) guidelines.
- Files should end with a new line.
- The first line of all files should be exactly `#!/usr/bin/env python3`.
- All modules, classes, and functions must have documentation.

## Project Structure
## Tasks To Complete

+ [x] 0. **Async Generator**<br/>[0-async_generator.py](0-async_generator.py) contains an asynchronous coroutine called `async_generator` that takes no arguments and meets the following requirements:
  + The coroutine will loop 10 times, each time asynchronously wait 1 second, then yield a random number between 0 and 10.
  + Use the `random` module.

+ [x] 1. **Async Comprehensions**<br/>[1-async_comprehension.py](1-async_comprehension.py) contains a script that meets the following requirements:
  + Import `async_generator` from the previous task and then write a coroutine called `async_comprehension` that takes no arguments.
  + The coroutine will collect 10 random numbers using an async comprehensing over `async_generator`, then return the 10 random numbers.

+ [x] 2. **Run time for four parallel comprehensions**<br/>[2-measure_runtime.py](2-measure_runtime.py) contains a script that meets the following requirements:
  + Import `async_comprehension` from the previous file and write a `measure_runtime` coroutine that will execute `async_comprehension` four times in parallel using `asyncio.gather`.
  + `measure_runtime` should measure the total runtime and return it.
