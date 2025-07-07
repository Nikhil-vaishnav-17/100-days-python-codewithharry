# Methods in dictionary

ep1 = {1 : 10, 3 : 30, 4 : 40}
ep2 = {2 : 20, 5 : 50, 1.5 : 15}

ep1.update(ep2)
print(ep1)
print(ep2)

'''
ep1.clear() : clear the dictionary

ep1.pop(1) : removes the 1 from the dictionary

ep1.popitem() : Pops the last element

del ep1 : deletes the dictionary

del ep1[1] : same as ep1.pop(1), if value dont exist it will throw an error


'''