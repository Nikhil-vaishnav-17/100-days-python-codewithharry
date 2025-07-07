#For loops
name = 'Chandrasekhar'
for i in name:
    print(i, end=', ') #prints every character, with ',' in between
print()
colours = ["Red", "Yellow", "Green", "Blue"]
for colour in colours:
    print(colour, end=": ")
    for i in colour:
        print(i, end=", ")
    print()

for i in range(5):
    print(i, end="\t") #0-4

print("\nNext loop: ")
for i in range(5,10): # 5-9
    print(i, end="\t")

print("\nNext loop: ")
for i in range(10,0,-2): # 10-0 and -2 decrement
    print(i, end="\t")
