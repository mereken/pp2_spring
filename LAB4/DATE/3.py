import datetime

dtime = datetime.datetime.now()
dtime_without_microseconds = dtime.replace(microsecond=0)
print(f'current dtime: {dtime}')
print(f'current dtime without microsecons: {dtime_without_microseconds}')
