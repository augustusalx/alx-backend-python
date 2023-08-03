#!/usr/bin/env python3
"""Contains a function with annotated parameters and
return values"""
from typing import Iterable, Sequence, List, Tuple


def element_length(lst: Iterable[Sequence]
                   ) -> List[Tuple[Sequence, int]]:
    """Returns list of tuples with the length of each element"""
    return [(i, len(i)) for i in lst]
