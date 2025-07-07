#Threading

import threading
import time


#It is a module which is used to perform multiple task in a single time

def func(seconds):
    print(f"Sleeping for {seconds} seconds")
    time.sleep(seconds)
    return seconds

time_start = time.perf_counter()

print(func(4))
print(func(2))
print(func(1))

time_end = time.perf_counter()
print(f"Total time to execute normally: {time_end- time_start}\n")

#IF we use threads we can run them parallely to avoid extra time taken
time_start = time.perf_counter()

t1 = threading.Thread(target=func, args=[4])
t2 = threading.Thread(target=func, args=[2])
t3 = threading.Thread(target=func, args=[1])

t1.start() #Starts the thread
t2.start()
t3.start()

t1.join() #Waits for the thread to complete
t2.join()
t3.join()

time_end = time.perf_counter()

print(f"\nTotal time to execute with threads: {time_end- time_start}")


#We can use concurrent.futures ThreadPoolExecutor to run them
from concurrent.futures import ThreadPoolExecutor

with ThreadPoolExecutor() as executor:
    time_start = time.perf_counter()

    future1 = executor.submit(func, 4)
    future2 = executor.submit(func, 2)
    future3 = executor.submit(func, 1)
    print(future1.result())
    print(future2.result())
    print(future3.result())

    time_end = time.perf_counter()

    print(f"\nTotal time to execute with ThreadPoolExecutor: {time_end - time_start}")

    l = [4,2,1]
    results = executor.map(func, l)
    for result in results:
        print(result)