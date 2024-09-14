from datetime import date
day, month = map(int, input().split())
data = date(2009, month, day)
print(data.strftime("%A"))
