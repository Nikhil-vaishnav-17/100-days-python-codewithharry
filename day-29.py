#Recursion in python
def factorial(n):
    if n == 1 or n == 0:
        return 1
    else:
        return n * factorial(n - 1)

print(factorial(5))

def fibonacci_series(n):
    if n == 1:
        return 1
    elif n == 0:
        return 0
    else:
        return fibonacci_series(n-1) + fibonacci_series(n-2)
print(fibonacci_series(15))