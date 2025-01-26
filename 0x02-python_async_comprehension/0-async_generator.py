#!/usr/bin/env python3
"""Task 0"""
import asyncio
import random
from typing import Generator


async def async_generator() -> Generator[float, None, None]:
    """Coroutine to generate 10 numbers between 0 and 10, 1s at a time"""
    for _ in range(10):
        await asyncio.sleep(1)
        yield random.random() * 10
