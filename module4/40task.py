from collections import deque
from typing import List

def rotate_list(nums: List[int], n: int):
    d = deque(nums)
    d.rotate(n)
    return list(d)

code = []
while data := input():
    code.append(data)
code = "\n".join(code)
exec(code)
