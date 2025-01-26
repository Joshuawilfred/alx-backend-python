#!/usr/bin/env python3
"""Task 2"""
import asyncio
import time
from importlib import import_module as imp


async_comprehension = imp('1-async_comprehension').async_comprehension


async def measure_runtime() -> float:
    """Returns the total runtime"""
    start_time = time.time()
    await asyncio.gather(*(async_comprehension() for _ in range(4)))
    return time.time() - start_time
