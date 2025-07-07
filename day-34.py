#else with for loops

for i in range(5):
    print(i)
else:
    print("Loop done")
#The else will only execute if the loop is completed. If it is break in between than it will not execute

i = 0
while i < 5:
    print(i)
    i += 1
else:
    print("Loop done")