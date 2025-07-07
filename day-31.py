#Methods in sets
s1 = {1,2,3,4}
s2 = {3,4,5,6}

print(s1.union(s2))
# s1.update(s2) : updates the s1 with union of s1 & s2
print(s1,s2)

print(s1.intersection(s2)) #Neither s1 nor s2 gets updated
# s1.intersection_update(s2) : updates the s1 with intersection of s1 & s2

print(s1.symmetric_difference(s2))
# s1.symmetric_difference_update(s2) : updates the s1 with symmetric difference of s1 & s2

print(s1.difference(s2)) # s1-s2
# s1.difference_update(s2) : updates the s1 with difference of s1 & s2

s1 = {1,2,3,4}
s2 = {1,2,3}
print(s1.isdisjoint(s2)) # checks if any element of s2 is present in s1 or not, if it is present then it will return false
print(s1.issuperset(s2)) #check if all the elements of s2 is present in s1 or not, if yes then returns true
print(s2.issubset(s1))

'''
s1.add(5) : add 5 to the set

s1.remove(5) : removes 5 from the set if it not present then it will show an error
s1.discard(5) : same as remove but it will not show any error if the value 5 is not present in the set

s1.pop() : removes the last item from the set but we dont know which will gets popped as sets are unordered list

del s1 : deletes a set s1

s1.clear() : deletes all the items and returns an empty set
'''

if 10 in s1:
    print("Yes")
else:
    print("False")