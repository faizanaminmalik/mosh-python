import time
from datetime import datetime

dt = datetime(2022, 1, 27)
print(dt)

dt = datetime.now()
print(dt)

dt = datetime.strptime("20-04-1991", "%d-%m-%Y")
print(dt)

dt = datetime.fromtimestamp(time.time())
print(dt)

print(dt.year)
print(dt.month)
print(dt.day)

# To print a custom formatted time
print(f"{dt.year}/{dt.month}/{dt.day}")
print(dt.strftime("%Y/%m/%d"))