import datetime

days, seconds = int(input()), int(input())

def shift_time(days: int, seconds: int):
    base_time = datetime.datetime(2023, 1, 1, 12, 30, 0)
    delta = datetime.timedelta(days=days, seconds=seconds)
    new_time = base_time + delta
    return (new_time.day, new_time.second)

print(shift_time(days, seconds))
