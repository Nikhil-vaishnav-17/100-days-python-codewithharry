#Raise errors in program

# x = int(input('Enter a value between 5 and 9: '))
#
# if 5 > x < 9:
#     raise ValueError('Enter the value between 5 and 9.')
# else:
#     print(x)

x = input('Enter a value between 5 and 9: ')

if x == 'quit':
    print('Okay')
elif 5 <= int(x) <= 9:
    print(x)
else:
    raise ValueError('Enter the value between 5 & 9')