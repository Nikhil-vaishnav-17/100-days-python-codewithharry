#Shorthand 'IF' 'else' statement
a = 10
b = 20
c = 30
print("A") if a > b and a > c else print("B") if b > a and b > c else print("C")

d = a if a > b and a > c else b if b > c and b > a else c
print(d)