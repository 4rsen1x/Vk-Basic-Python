n = int(input())
print(";".join(map(str, sorted((max(map(int, input().split())) for _ in range(n)), reverse=True))))
