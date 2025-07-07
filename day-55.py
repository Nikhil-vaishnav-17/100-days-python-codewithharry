#Rock paper scissors game
import random

def print_choice(choice, chooser):
    if choice == -1:
        print(f"{chooser} choice is Rock")
    elif choice == 0:
        print(f"{chooser} choice is Paper")
    elif choice == 1:
        print(f"{chooser} choice is Scissors")

def check_winner(user_c, computer_c) -> None:
    if user_c == computer_c:
        print_choice(user_c, 'Your')
        print_choice(computer_c, 'Computer')
        global draw
        draw += 1
        print('Draw')
    elif (user_c == -1 and computer_c == 0) or (user_c == 0 and computer_c == 1) or (user_c == 1 and computer_c == -1):
        print_choice(user_c, 'Your')
        print_choice(computer_c, 'Computer')
        global lose
        lose += 1
        print('You Lost')
    elif (user_c == -1 and computer_c == 1) or (user_c == 0 and computer_c == -1) or (user_c == 1 and computer_c == 0):
        print_choice(user_c, 'Your')
        print_choice(computer_c, 'Computer')
        print('You Won')
        global win
        win += 1

def print_score():
    print("Current score is: ")
    global draw, win, lose

    if win == lose:
        print("Draw ", end="")
    elif win < lose:
        print(f"Computer in lead by {lose-win} points ", end="")
    else:
        print(f"User in lead by {win-lose} points ", end="")

    print(f"with score: Draw {draw}, Won {win} and Lost {lose}")

win, lose, draw = 0, 0, 0
while True:
    try:
        print("\nEnter -1 for Rock, 0 for Paper, 1 for Scissors and other Number to exit.")
        user_choice = int(input("Enter your choice: "))
    except ValueError:
        print("Enter a number of the choice.")
        continue

    if -1 <= user_choice <= 1:
        computer_choice = random.choices(range(-1,2))[0]
        check_winner(user_choice, computer_choice)
        print_score()
    else:
        print('\nIt was fun playing with you, Hope you will come soon')
        print_score()
        break