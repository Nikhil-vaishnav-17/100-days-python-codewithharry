#Local and Global variable

x = 4
print(x)

def func():
    global x #This will use the global variable 'x'
    x = 5
    # print(x)

print("The global variable is: ", x)
func()
print("The global variable is: ", x)
