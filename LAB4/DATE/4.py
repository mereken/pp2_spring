import datetime

date_1 = datetime.datetime(2024, 2, 21, 12, 0, 0)
date_2 = datetime.datetime(2024, 3, 2, 12, 0, 0)

diff = (date_2 - date_1).total_seconds()
print ('difference between two dates: ', diff)
