#Match statements: switch case in c or c++
x = int(input("Enter a number: "))
match x:
    case 1 :
        print("X is 1")
    case _ if x % 2 == 0 : # default case with if condition
        print("Number is even")
    case _ if x < 0 :
        print("No is negative")
    case _ :  # default condition
        print("Hello")