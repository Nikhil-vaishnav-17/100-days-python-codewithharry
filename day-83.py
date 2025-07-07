#Time module

import time

t1 = time.localtime()
formated_time = time.strftime("%Y/%m/%d - %H:%M:%S", t1)
print("Lets wait for some time before printing it")
time.sleep(3)
print(formated_time)