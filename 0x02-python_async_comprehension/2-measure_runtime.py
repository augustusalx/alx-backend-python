#!/usr/bin/env python3
'''Module for task 2
'''
import asyncio
import time
from importlib import import_module as using


async_comprehension = using('1-async_comprehension').async_comprehension


async def measure_runtime() -> float:
    '''to execute async_comprehension 4 times and measure the
    total time for execution
    '''
    start_time = time.time()
    await asyncio.gather(*(async_comprehension() for _ in range(4)))
    return time.time() - start_time
