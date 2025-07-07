#typecasting
a = "1"
b = "2"

print(a+b) #12
print(int(a) + int(b)) #3

#implicit typecasting (python compiler khud karta hai)
a = 8
b = 1.9
c = a+b
print(a, type(a))
print(b, type(b))
print(c, type(c))