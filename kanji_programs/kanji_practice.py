# Built-in Imports
import argparse
from getpass import getpass
import json
from os import system
from random import shuffle
from sys import exit


def main():
    clear_console()

    user_score = 0
    # Stores the number of the questions answers wrong (ie, questions 2, 3, and 6)
    questions_answered_wrong = []
    user_incorrect_answers = []

    args = init_command_line_args()

    # File must end with .txt extension or .json extension for program to run
    if not args.filename.endswith(".json") and not args.filename.endswith(".txt"):
        handle_exception("File extension is not compatible with program! File must end with .txt or .json extension.\n\nPress enter to exit program. ")

    # Ensure file exists before running additional code
    try:
        f = open(args.filename)
    except FileNotFoundError:
        handle_exception("File not found! Make sure the file is in the working directory.\n\nPress enter to exit program. ")
    else:
        with f:
            # Ensure file is not empty before running additional code
            if file_empty(f):
                f.close()
                handle_exception("The file cannot be read from because it is empty.\n\nPress enter to exit program. ")
            else:
                # Reset file pointer position after running file_empty() function
                f.seek(0)

                # Ensure file is in proper json format
                try:
                    vocab_set = json.load(f)
                except:
                    f.close()
                    handle_exception("The file cannot be used because it is formatted incorrectly (must be a json).\n\nPress enter to exit program. ")


    f.close()

    shuffle(vocab_set)

    # Variables contain the starting mode (kanji or English) and the ending mode (English or kana) for the chosen study method
    study_modes = select_study_method()

    # Study method 1: English to kana
    if study_modes[0] == "english" and study_modes[1] == "kana":
        for i, shuffled_entry in enumerate(vocab_set):
            print(f"Word: {shuffled_entry['english'].title()}")
            user_translation = input("Type the hiragana translation: ")

            # If the user's translation is correct, add 1 to user_score
            if user_translation == shuffled_entry["kana"]:
                user_score += 1
            else:
                user_incorrect_answers.append(user_translation)
                questions_answered_wrong.append(i)
            clear_console()

    # Study method 2: Kanji to English
    elif study_modes[0] == "kanji" and study_modes[1] == "english":
        for i, shuffled_entry in enumerate(vocab_set):
            print(f"Kanji: {shuffled_entry['kanji']}")
            user_translation = input("Type the English word for the kanji: ")

            # If the user's translation is correct, add 1 to user_score
            if user_translation == shuffled_entry["english"]:
                user_score += 1
            else:
                user_incorrect_answers.append(user_translation)
                questions_answered_wrong.append(i)
            clear_console()

    # Study method 3: Kanji to kana
    else:
        for i, shuffled_entry in enumerate(vocab_set):
            print(f"Word: {shuffled_entry['kanji']}")
            user_translation = input("Type the hiragana translation: ")

            # If the user's translation is correct, add 1 to user_score
            if user_translation == shuffled_entry["kana"]:
                user_score += 1
            else:
                user_incorrect_answers.append(user_translation)
                questions_answered_wrong.append(i)
            clear_console()

    print_score(user_score, vocab_set, user_incorrect_answers, questions_answered_wrong, study_modes)

    proceed("Press enter to exit the program. ")
    clear_console()



def handle_exception(prompt):
    proceed(prompt)
    clear_console()
    exit()


def select_study_method():
    print("How would you like to study?\n")
    print("1. English to kana - *Best for learning the reading/spelling for a word*")
    print("2. Kanji to English - *Best for associating kanji with its English word*")
    print("3. Kanji to kana - *Best for associating kanji with its reading*\n")

    while True:
        try:
            study_method_choice = int(input("Enter the number of the studying method you wish to use: "))
            if study_method_choice < 1 or study_method_choice > 3:
                raise ValueError
            break
        except ValueError:
            clear_console()
            print("How would you like to study?\n")
            print("1. English to kana - *Best for learning the reading/spelling for a word*")
            print("2. Kanji to English - *Best for associating kanji with its English word*")
            print("3. Kanji to kana - *Best for associating kanji with its reading*\n")
            print("Invalid number entered! Please try again: ")

    match study_method_choice:
        case 1:
            start_mode = "english"
            end_mode = "kana"
        case 2:
            start_mode = "kanji"
            end_mode = "english"
        case 3:
            start_mode = "kanji"
            end_mode = "kana"

    clear_console()

    return (start_mode, end_mode)


#Initializes the command-line args for this specific program
def init_command_line_args():
    parser = argparse.ArgumentParser(description="Program for studying kanji translation to English or kana")
    parser.add_argument("-f", "--filename", help="pass a .txt file to the program", type=str, required=True)

    args = parser.parse_args()

    return args


def print_score(user_score, vocab_set, user_incorrect_answers, questions_answered_wrong, study_modes):
    clear_console()
    max_score = len(vocab_set)

    if user_score == max_score:
        print(f"Score: {user_score}/{max_score}.\nYou have no enemies.\n")
    else:
        print(f"Score: {user_score}/{max_score}.\n")
        show_corrections(user_incorrect_answers, questions_answered_wrong, vocab_set, study_modes)


def show_corrections(user_incorrect_answers, questions_answered_wrong, vocab_set, study_modes):
    for i in range(len(user_incorrect_answers)):
        print(f"Your translation of {vocab_set[questions_answered_wrong[i]][study_modes[0]]}: {user_incorrect_answers[i]}\nCorrect translation of {vocab_set[questions_answered_wrong[i]][study_modes[0]]}: {vocab_set[questions_answered_wrong[i]][study_modes[1]]}\n")


#Checks if a file is empty
def file_empty(file):
    #Move file pointer to start of file
    file.seek(0)
    #If the first character of the file cannot be read, return True (file is empty), else False
    if not file.read(1):
        return True
    return False


# Prompts the user before proceeding with the program
def proceed(prompt):
    # Hides user input + doesn't store it -> Program pauses until the user presses Enter
    getpass(prompt)


# Clears the console
def clear_console():
    # Clears the terminal when run
    system("clear")


if __name__ == "__main__":
    main()
