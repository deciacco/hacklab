#main thread

from calendar import c
import threading, time
from datetime import datetime

def sleeper(i):
    print("hello from %d!" % i)
    time.sleep(i)
    print("goodbey from %d!" % i)

#print(datetime.now().strftime("%H:%M:%S"))
"""
sleeper(0)
sleeper(1)
sleeper(2)
sleeper(3)

threading.Thread(target=sleeper, args=(0,)).start()
threading.Thread(target=sleeper, args=(1,)).start()
threading.Thread(target=sleeper, args=(2,)).start()
threading.Thread(target=sleeper, args=(3,)).start()
"""

#Wait to start in 5 seconds and pass in the arg 5
#threading.Timer(5, sleeper, [1]).start()

#print(datetime.now().strftime("%H:%M:%S"))

#************************************************************
"""
stop = False

def input_thread():
    global stop

    while True:
        user_input = input("Should we stop?: ")
        print(">> User says: {}".format(user_input))

        if user_input == "yes":
            stop = True
            break

def output_thread():
    global stop

    count = 0

    while not stop:
        print(count)
        count += 1
        time.sleep(1)

t1 = threading.Thread(target=input_thread).start()
t2 = threading.Thread(target=output_thread).start()
"""
#************************************************************

#race condition trying to access save variable at same time
#threading lock, preventing simultanious modification of a variable

def sync_consume_thread():
    global data, data_lock

    while True:
        time.sleep(1)

        data_lock.acquire()
        if len(data) > 0:
            print(threading.current_thread().name, data.pop(), len(data))          
        data_lock.release()

        if len(data) == 0:
            print("breaking")
            break

data_lock = threading.Lock()
data = [x for x in range(20)]

threading.Thread(target=sync_consume_thread).start()
threading.Thread(target=sync_consume_thread).start()
threading.Thread(target=sync_consume_thread).start()