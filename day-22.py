#Lists
list1 = [1,2,3,4,'harry']

print(list1)
print(type(list1))
print(list1[1])
print(list1[4])

#It can have negative indexing means it will give the last n th element
print(list1[-2])
print(list1[len(list1)-2])
print(list1[5-2])
print(list1[3])

#It can search the items directly
if 'harry' in list1:
    print("Yes")
else:
    print("No")

#it can also be used in strings
if 'n' in 'abcdefghijklmnopqrstuvwxyz':
    print("Yes")

#you can print the list in a range
print(list1[1:3])

#you can use a jump index
list2 = [1,2,3,4,5,6,7,8,9,10]
print(list2[1:8:2]) #it will print the values in range 1-8 and with 2 as difference in indexing

#list comprehension
list3 = [i*i for i in range(10) if i%2 == 0]
print(list3)

names = ["nikhil",'himanshu', 'badal', 'parth']
list4 = [n for n in names if 'i' in n]
print(list4)