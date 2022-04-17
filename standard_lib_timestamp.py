# In python we have 2 libraries to work with time
# time and datetime
# time works on timestamp i.e no. of days after Jan 1 1970
import time

print(time.time())

def send_email():
    for i in range(1000000):
        pass

start_time = time.time()
send_email()
end_time  = time.time()

duration = end_time - start_time
print("duration : ", duration)