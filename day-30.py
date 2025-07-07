#sets in python
sets = {1,2,3,2,4,2,5,2}
print(type(sets), sets)

# to create an empty set
empty_set = {} #Will be a dictionary
print(type(empty_set))

empty_set = set()
print(type(empty_set))

for i in sets:
    print(i,end=', ')