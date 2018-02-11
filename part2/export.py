from reports import *
from printing import greetings

question_arguments = {
                "1": "Please enter filename: ",
                "2": "Please enter filename: ",
                "3": "Please enter filename: ",
                "4": "Please enter filename:",
                "5": "Please enter filename: ",
                "6": "Please enter filename and title separated by coma: ",
                "7": "Please enter filename: ",
                "8": "Please enter filename: ",
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

user_input = ""
greetings()
export_file = input("Enter file name for export: " )
answers_to_export = []
while True:
    arguments = []
    user_input = input("\nChoose option:")
    if user_input == "9":
        break
    if user_input not in question_no_to_function:
        print("Oops, option not found. Please try again")
        continue
    if user_input in question_arguments:
        arguments = input(question_arguments[user_input])
        arguments = arguments.strip().split(",")
    try:
        if user_input in question_no_to_function:
            answers_to_export.append(question_no_to_function[user_input](*arguments))
    except(ValueError, TypeError):
        print("Entered arguments aren't correct. Please try again.")

with open(export_file, mode='a', encoding='utf-8') as f:
    for answer in answers_to_export:
        f.write("{}\n".format(str(answer)))

