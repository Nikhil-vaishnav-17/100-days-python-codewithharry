#Finally keyword in exceptional handling

try:
    x = int(input("Enter the index you want to check: "))
    l = [1,2,3,4,5]
    print(l[x])
except IndexError:
    print('Index not found')
finally:
    print('End of program')

#The use of finally keyword is that it will always execute.
#Well you can say you can put it outside the 'finally' keyword and still it will be executed.
#The good thing lies when you use it in a function

def func() -> bool:
    try:
        x = int(input("Enter the index you want to check: "))
        l = [1, 2, 3, 4, 5]
        print(l[x])
        return True
    except IndexError:
        print('Index not found')
        return False
    finally:
        print('End of program')
#If you don't use finally keyword that that block of code will never be executed. It can be useful in file handling
x = func()
print(x)