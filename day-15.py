import time

timestamp = time.strftime('%H:%M:%S')
print(timestamp)
timestamp = time.strftime('%H')
print(timestamp)
timestamp = time.strftime('%M')
print(timestamp)
timestamp = time.strftime('%S')
print(timestamp)

timestamp = int(time.strftime('%H'))
if 6 < timestamp < 12:
    print("Good morning")
elif 12 <= timestamp < 18:
    print("Good afternoon")
else:
    print("Good night")
