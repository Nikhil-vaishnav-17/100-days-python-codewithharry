#Functions with different arguments

def average(a = 1 , b = 1):
    print("Average of the 2 numbers are", (a+b)/2)

average()
average(4,6)
average( b=9 )
average( b=10 , a=15)

#You can create a multi variable function by taking the argument as tuple
def SumOfNum(*numbers):
    total = 0
    for i in numbers:
        total = total + i

    print("The sum is", total)

SumOfNum(1,2)
SumOfNum(2,3,4)
SumOfNum(3,6,12,64)

#you can also return a value in the program
def square(a):
    return a*a

b = square(5)
print(b)
print(square(10))
