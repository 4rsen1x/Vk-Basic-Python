def cache_deco(func):
    cache = {}
    def wrapper(*args, **kwargs):
        key = (args, tuple(sorted(kwargs.items())))
        if key not in cache:
            cache[key] = func(*args, **kwargs)
        return cache[key]
    return wrapper

def solution(func_map, func_filter, data):
    count = 0
    for item in data:
        if func_filter(item):
            mapped = func_map(item)
            if count % 2 == 0:
                yield mapped
            count += 1
code = []
while data := input():
  code.append(data)
code = "\n".join(code)
exec(code)
