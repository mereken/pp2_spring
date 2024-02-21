import datetime

today = datetime.date.today()
tdelta = datetime.timedelta(days=1)
yesterday = today - tdelta
tomorrow = today + tdelta

print(f'today is {today}')
print(f'yesterday was {yesterday}')
print(f'tomorrow will be {tomorrow}')