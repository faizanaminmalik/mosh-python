from datetime import datetime, timedelta

dt1 = datetime(2020,1,1)
print(dt1)

dt2 = datetime.now()
print(dt2)

dif = dt2 - dt1
print(dif) # will show delta like 837 days, 5:43:37.23421

print("days: ", dif.days)
print("seconds: ", dif.seconds)
print("total_seconds : ", dif.total_seconds())