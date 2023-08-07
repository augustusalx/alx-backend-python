#!/usr/bin/env python3
""" Import wait_n into 2-measure_runtime.py from the previous file.
    measure the total execution time for wait_n(n, max_delay), and
    returns total_time. """
import asyncio
import time
wait_n = __import__('1-concurrent_coroutines').wait_n


def measure_time(n: int, max_delay: int) -> float:
    """ Measure the runtime """
    start_time = time.time()
    asyncio.run(wait_n(n, max_delay))
    end_time = time.time()
    total_time = end_time - start_time
    return total_time / n
