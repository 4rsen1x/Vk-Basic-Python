from typing import List, Dict

def make_most_common_keys(d: Dict[int, int]) -> List[int]:
    return [key for key, _ in sorted(d.items(), key=lambda item: item[1], reverse=True)]

code = []
while data := input():
    code.append(data)
code = "\n".join(code)
exec(code)
