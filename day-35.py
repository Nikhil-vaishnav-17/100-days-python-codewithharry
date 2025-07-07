#Exceptional handling


while True:
    a = input('Enter a input: ')
    try:
        for i in range(1,11):
            print(f"{a} X {i} = {int(a) * i}")
    except ValueError:
        print('Invalid input! input should be a number')
        continue
    break


a = [1,2,3]
try:
    b = int(input('Enter a integer: '))
    print(a[b])
except ValueError:
    print('Input should be an integer and should be in range')
except IndexError:
    print('No is greater than what it should be')