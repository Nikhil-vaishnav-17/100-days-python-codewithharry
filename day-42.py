#Enumerate function usage

marks = [1,2,3,4,5,6,7,8,9,10]

j = 0
for i in marks:
    print(i)
    if j == 5:
        print("Hii")
    j += 1
#The above code is waste as it is not good
#We can use enumerate function for this directly

for index, number in enumerate(marks):
    print(number)
    if index == 5:
        print("Hii")
#This works as same as the above code
#We can also specify the starting value of index like: enumerate(marks, start=1) : this will make the index to start with 1