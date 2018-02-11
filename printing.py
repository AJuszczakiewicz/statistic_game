from reports import *

question_arguments = {
                "1": "Please enter filename: ",
                "2": "Please enter filename and year separating them by coma: ",
                "3": "Please enter filename: ",
                "4": "Please enter filename and genre separating them by coma:",
                "5": "Please enter filename and title separating them by coma: ",
                "6": "Please enter filename: ",
                "7": "Please enter filename: ",
                "8": "Please enter filename: ",
             }

question_no_to_function = {
                    "1": count_games,
                    "2": decide,
                    "3": get_latest,
                    "4": count_by_genre,
                    "5": get_line_number_by_title,
                    "6": sort_abc,
                    "7": get_genres,
                    "8": when_was_top_sold_fps,
                    "9": exit
                        }


def greetings():
    print("Welcome in new statistic program wrote just for you!")
    print("To choose question you are seeking answer to, enter question number:")
    print("1. How many games are in the file? ")
    print("2. Is there a game from a given year? ")
    print("3. Which was the latest game?")
    print("4. How many games do we have by genre?")
    print("5. What is the line number of the given game (by title)?")
    print("6. What is the alphabetical ordered list of the titles?")
    print("7. What are the genres?")
    print("8. What is the release date of the top sold 'First-person shooter' game?")
    print("For exit, enter: 9")


greetings()
while True:
    arguments = []
    user_input = input("\n:")
    if user_input in question_arguments:
        arguments = input(question_arguments[user_input])
        arguments = arguments.strip().split(",")
    if user_input in question_no_to_function:
        print(question_no_to_function[user_input](*arguments))
