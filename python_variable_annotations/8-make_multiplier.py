#!/usr/bin/env python3
"""
    8. Complex types - functions
"""
from typing import Callable


def make_multiplier(multiplier: float) -> Callable[[float], float]:
    """returns a function that multiplies a float by multiplier"""
    def multiplier_function(x: float) -> float:
        """Multiply a float by the multiplier"""
        return multiplier * x

    return multiplier_function
