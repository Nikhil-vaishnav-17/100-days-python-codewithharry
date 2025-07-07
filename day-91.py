#Generators

#Generators are special type of functions which terminate the function and resume when next function is called
#instead of 'return' it uses 'yield'

def my_generator():
    for i in range(100):
        yield i

mygen = my_generator()
print(next(mygen))
print(next(mygen))
print(next(mygen))

