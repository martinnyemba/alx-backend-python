#!/usr/bin/env python3
'''
An async routine called wait_n that takes in 2 int arguments: n and max_delay.
spawn wait_random n times with the specified max_delay.
wait_n return the list of all the delays (float values).
The list of the delays is  in ascending order without using sort()
because of concurrency.
'''
import asyncio
from typing import List


wait_random = __import__('0-basic_async_syntax').wait_random


async def wait_n(n: int, max_delay: int) -> List[float]:
    '''Executes wait_random n times.
    '''
    wait_times = await asyncio.gather(
        *tuple(map(lambda _: wait_random(max_delay), range(n)))
    )
    return sorted(wait_times)
