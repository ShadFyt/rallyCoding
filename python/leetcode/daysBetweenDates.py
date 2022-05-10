import datetime


def solve(date1: str, date2: str) -> int:
    day1 = date1.split("-")
    day2 = date2.split("-")
    formatted_date1 = datetime.date(int(day1[0]), int(day1[1]), int(day1[2]))
    formatted_date2 = datetime.date(int(day2[0]), int(day2[1]), int(day2[2]))
    return abs(formatted_date2 - formatted_date1).days


print(solve("2020-01-15", "2019-12-31"))
print(solve("2019-06-29", "2019-06-30"))
print(solve("2019-06-29", "2019-06-29"))
print(solve("1971-06-29", "2010-09-23"))
