#Methods in tuples
#You cannot change tuple directly, but you can do it after changing it to list
#Like this
tup = (1,2,3,4)
print(type(tup), tup)
temp = list(tup)
temp.append(5) # adds 5 in last
temp.pop(3) # removes 3rd index = 4
temp[0] = 0 #Makes the first element to 0
tup = tuple(temp)
print(type(tup), tup)

'''
We can merge 2 tuples with + operator:
tup3 = tup1 + tup2

tup.count(1) : gives the occurrence of 1 in the tuple

tup.index(1) : gives the index of first occurrence of 1

tup.index(1,3,10) : slices the tuple from 3-10 and find the first occurrence of 1
'''