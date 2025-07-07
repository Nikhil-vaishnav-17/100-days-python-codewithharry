age = int(input("Enter the age: "))
print("Your age is:", age)

# Conditional operators
# <, >, <=, >=, ==, !=
if age > 60:
    print("You need to give a driving test")
elif age >= 18:
    print("You can drive")
else:
    print("You cannot drive")

if age >= 18:
    if age > 60:
        print("You need to give a driving test")
    elif age > 40:
        print("You are okay")
    else:
        print("You can drive")
elif age <= 0:
    print("Age should be valid")
else:
    print("You are a child")

# For multiple condition in same if statement you can you 'and' 'or' statement in between
# example: if age >= 18 and age < 60