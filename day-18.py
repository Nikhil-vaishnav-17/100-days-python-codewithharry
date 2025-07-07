#While loop
i = 1
while i <= 10:
    print(i, end=" ")
    i = i+1

#We can use else with while loop
print()
i = int(input("Enter i: "))
while i < 5:
    print(i, end=" ")
    i = i + 1
else:
    print("Out of while loop")
# There is no do-while loop in python, but we can create one on our own.
#Like if we want to print the number from user input to 10 but do while will run 1 iteration before checking the condition

i = int(input("Enter i: "))
while True:
    if i == 5:
        i = i + 1
        continue
    print(i, end=" ")
    i = i + 1
    if i > 10:
        break