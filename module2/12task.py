def average_from_string(s):
    numbers = list(map(int, s.split()))
    avg = sum(numbers) / len(numbers)
    result = f"{avg:.2f}"
    if result[-1] == "0":
        result = result[:-1]
    return result

while True:
    line = input()
    if line == "":
        break
    print(average_from_string(line))
