from reports import *


question_arguments = {
                "1": "Please enter filename: ",
                "2": "Please enter filename and year separating them by coma: ",
                "3": "Please enter filename: ",
                "4": "Please enter filename and genre separating them by coma:",
                "5": "Please enter filename and title separating them by coma: ",
                "6": "Please enter filename: ",
                "7": "Please enter filename: ",
                "8": "Please enter filename: "
             }

question_no_to_function = {
                    "1": get_most_played,
                    "2": sum_sold,
                    "3": get_selling_avg,
                    "4": count_longest_title,
                    "5": get_date_avg,
                    "6": get_game,
                    "7": count_grouped_by_genre,
                    "9": exit
                        }


def greetings():
    print("Welcome in new statistic program wrote just for you!")
    print("To choose question you are seeking answer to, enter question number:")
    print("1. What is the title of the most played game (i.e. sold the most copies)?")
    print("2. How many copies have been sold total?")
    print("3. What is the average selling?")
    print("4. How many characters long is the longest title?")
    print("5. What is the average of the release dates?")
    print("6. What properties has a game?")
    print("7. How many games are there grouped by genre?")
    print("8. What is the date ordered list of the games? ")
    print("For exit, enter: 9")


user_input = ""
greetings()
while user_input is not "9":
    arguments = []
    user_input = input("\n:")
    if user_input not in question_no_to_function:
        print("Oops, option not found. Please try again")
        continue
    if user_input in question_arguments:
        arguments = input(question_arguments[user_input])
        arguments = arguments.strip().split(",")
    try:
        if user_input in question_no_to_function:
            print(question_no_to_function[user_input](*arguments))
    except ValueError:
        print("Entered arguments aren't correct. Please try again.")

