#'lambda' functions
#Lambda is a one-liner function which can be used by lambda keywords
def add_five(fx, value):
    return 5 + fx(value)
double = lambda x: x*2
cube = lambda x : x**3
print(double(10), cube(5))
print(add_five(cube,2))