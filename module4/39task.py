import datetime
from collections import Counter
from typing import List

def most_common_months(dates: List[str], n) -> List[int]:
    months = []
    for date_str in dates:
        date = datetime.datetime.strptime(date_str, "%Y-%m-%dT%H:%M:%S")
        months.append(date.month)
    month_counts = Counter(months)
    return [month for month, _ in month_counts.most_common(n)]

code = []
while data := input():
    code.append(data)
code = "\n".join(code)
exec(code)
