#Who will be millionaire question
questions = ["Question 1", "Question 2", "Question 3", "Question 4", "Question 5", "Question 6", "Question 7", "Question 8",
             "Question 9", "Question 10", "Question 11", "Question 12", "Question 13", "Question 14", "Question 15", "Question 16"]
options = [["Option 1.1", "Option 1.2", "Option 1.3", "Option 1.4"],
           ["Option 2.1", "Option 2.2", "Option 2.3", "Option 2.4"],
           ["Option 3.1", "Option 3.2", "Option 3.3", "Option 3.4"],
           ["Option 4.1", "Option 4.2", "Option 4.3", "Option 4.4"],
           ["Option 5.1", "Option 5.2", "Option 5.3", "Option 5.4"],
           ["Option 6.1", "Option 6.2", "Option 6.3", "Option 6.4"],
           ["Option 7.1", "Option 7.2", "Option 7.3", "Option 7.4"],
           ["Option 8.1", "Option 8.2", "Option 8.3", "Option 8.4"],
           ["Option 9.1", "Option 9.2", "Option 9.3", "Option 9.4"],
           ["Option 10.1", "Option 10.2", "Option 10.3", "Option 10.4"],
           ["Option 11.1", "Option 11.2", "Option 11.3", "Option 11.4"],
           ["Option 12.1", "Option 12.2", "Option 12.3", "Option 12.4"],
           ["Option 13.1", "Option 13.2", "Option 13.3", "Option 13.4"],
           ["Option 14.1", "Option 14.2", "Option 14.3", "Option 14.4"],
           ["Option 15.1", "Option 15.2", "Option 15.3", "Option 15.4"],
           ["Option 16.1", "Option 16.2", "Option 16.3", "Option 16.4"]]
answers = [1,2,3,4,1,2,3,4,1,2,3,4,1,2,3,4]
selected = []
price = ['1k','2k','3k','5k','10k','20k','40k','80k','1.6L','3.2L','6.4L','12.5L','25L','50L','1Cr','7Cr']

for question_index, i in enumerate(questions):
    print(i)
    # question_index = questions.index(i)
    print(f"a) {options[question_index][0]}\t\t b) {options[question_index][1]}\nc) {options[question_index][2]}\t\t d) {options[question_index][3]}")

    while True:
        selected_option = int(input("Enter the selected option 1, 2, 3 or 4: "))
        if 1 <= selected_option <= 4:
            break

    selected.append(selected_option)
    if selected[question_index] == answers[question_index]:
        print("You are correct")
        print("You won", price[question_index], "\n")
    else:
        print("Selected option is wrong, the correct answer is", answers[question_index])
        if 0 <= question_index < 5:
            print("You didn't won anything")
        elif 5 <= question_index < 10 :
            print("Final winnings", price[4])
        elif 10 <= question_index < 15:
            print("Final winnings", price[9])
        elif question_index == 15 and selected[len(selected)-1] == answers[len(answers)-1]:
            print("Final winnings", price[15])
        else:
            print("Final winnings", price[9])
        break