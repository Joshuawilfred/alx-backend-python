#!/usr/bin/env python3
"""Task 1"""
from typing import List
from importlib import import_module


async_generator = import_module('0-async_generator').async_generator


async def async_comprehension() -> List[float]:
    """Return the 10 random numbers collected using async_generator"""
    return [num async for num in async_generator()]
