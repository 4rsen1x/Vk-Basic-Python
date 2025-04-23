start, end, step = map(int, input().split())
for x in map(lambda x: x**2 if x % 2 else -x, range(start, end, step)):
    print(x)
