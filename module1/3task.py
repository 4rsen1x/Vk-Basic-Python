left = int(input())
right = int(input())
numbers = []

while True:
    s = input()
    if s == "":
        break
    numbers.append(int(s))

all_in_range = all(left <= num <= right for num in numbers)
print(all_in_range)
