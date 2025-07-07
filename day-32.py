#Dictionaries in python
dic = {
    '156' : "Nikhil Vaishnav",
    155 : "Jangid",
    97 : "Himanshu",
    160 : "Rahul"
}

print(dic[156],dic[160]) #this method shows an error if the value doesn't exist
print(dic.get(156))  # this method does not show an error instead it will print NONE in that place
print(dic.keys()) # it will print all the keys of the dictionary like in thi scase its 155,156,97 etc

#You can also print all the values in the dict by using loops
for keys in dic.keys():
    # print(keys, ':',dic[keys])
    print(f"{keys} : {dic[keys]}")

print(dic.items()) #print all the keys with values in it
