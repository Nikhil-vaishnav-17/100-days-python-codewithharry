#Decorator
#It is a function which takes a func as argument and returns a new func that modifies the behaviour of the Original func

def greet(fx):
    def greeting(*args, **kwargs):
        print('Good morning')
        fx(*args, **kwargs)
        print('Thank you for using the function\n')
    return greeting

@greet
def hello():
    print('Hello world!')

@greet
def add(a,b):
    print(a+b)

hello()
add(5,6)
#If we don't add the @greet in the function of hello we can simply do: greet(fx)()
