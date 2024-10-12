#!/usr/bin/env python3
"""Task 7"""
from typing import Union, Tuple


def to_kv(k: str, v: Union[int, float]) -> Tuple[str, float]:
    """Returns a tuple from string k and number v"""
    return (k, float(v**2))
