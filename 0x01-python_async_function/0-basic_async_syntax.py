#!/usr/bin/env python3
'''
Asynchronous coroutine that takes in an integer

Argument:
    max_delay, with a default value of 10) named wait_random
    waits for a random delay between 0 and max_delay
'''
import asyncio
import random


async def wait_random(max_delay: int = 10) -> float:
    '''Waits for a random number of seconds.
    '''
    wait_time = random.random() * max_delay
    await asyncio.sleep(wait_time)
    return wait_time
