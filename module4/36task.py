from itertools import zip_longest
from typing import List, Tuple

def fill_missing_values(values_list_1: List[int], values_list_2: List[int]) -> List[Tuple[int, int]]:
    return [(x if x is not None else 1, y if y is not None else 1) 
            for x, y in zip_longest(values_list_1, values_list_2, fillvalue=None)]

code = []
while data := input():
    code.append(data)
code = "\n".join(code)
exec(code)
