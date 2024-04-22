#!/usr/bin/env python3
"""
    function sum_mixed_list which takes a list mxd_lst
    of integers and floats and returns their sum as a float.
"""
from typing import List, Union


def sum_mixed_list(mxd_lst: List[Union[int, float]]) -> float:
    """
        Sum a list of integers and floats.

        Parameters:
            mxd_lst (List[Union[int, float]]): The list of integers and floats.

        Returns:
            float: The sum of the integers and floats in the list.
    """
    return sum(mxd_lst)
