import time
def watchdog():
    time.sleep(10)
    f= open("trigger", 'w')
    f.write('1\n Watchdog found an error')
    f.close()
    print("wrote")