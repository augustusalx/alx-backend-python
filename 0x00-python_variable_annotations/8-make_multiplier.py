#!/usr/bin/env python3
"""Contains the function that multiplies a float by multiplier"""
from typing import Callable


def make_multiplier(multiplier: float) -> Callable[[float], float]:
    """Multiply a float by multiplier
    Args:
        multiplier (float): The multiplier
    Returns:
        A function that multiplies a float by multiplier
    """

    def multiplier_func(number: float) -> float:
        """Multiply a float by multiplier"""
        return multiplier * number

    return multiplier_func
