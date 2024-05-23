# Built-in Imports
import argparse
from getpass import getpass
import json
from os import system
from random import shuffle
from sys import exit


def main():
    clear_console()
    score = 0
    user_answers = {}
    questions_answered_wrong = []
    user_incorrect_answers = []

    args = init_command_line_args()

    # File must end with .txt extension for program to run
    if not args.filename.endswith(".txt"):
        exit("File passed is not a .txt file!")

    # Ensure file exists before running additional code
    try:
        f = open(args.filename)
    except FileNotFoundError:
        proceed("File not found! Make sure the file is in the working directory.\n\nPress enter to exit program. ")
        clear_console()
        exit()
    else:
        with f:
            # Ensure file is not empty before running additional code
            if file_empty(f):
                proceed("The file cannot be read from because it is empty.\n\nPress enter to exit program. ")
                clear_console()
                f.close()
                exit()
            else:
                # Reset file pointer position after running file_empty() function
                f.seek(0)

                # Ensure file is in proper json format
                try:
                    vocab_set = json.load(f)
                except:
                    proceed("The file cannot be read because it is formatted incorrectly.\n\nPress enter to exit program. ")
                    clear_console()
                    f.close()
                    exit()

                shuffle(vocab_set)

                for i, shuffled_entry in enumerate(vocab_set):
                    print(f"Kanji: {shuffled_entry['kanji']}")
                    user_translation_eng = input("Type the English word for the kanji: ")

                    # If the user's translation is correct, add 1 to score
                    if user_translation_eng == shuffled_entry["english"]:
                        score += 1
                    else:
                        user_incorrect_answers.append(user_translation_eng)
                        questions_answered_wrong.append(i)

                    clear_console()

                print_score(score, vocab_set, user_incorrect_answers, questions_answered_wrong)

                proceed("Press enter to exit the program. ")
                clear_console()
                f.close()


#Initializes the command-line args for this specific program
def init_command_line_args():
    parser = argparse.ArgumentParser(description="Program for studying kanji translation to English or kana")
    parser.add_argument("-f", "--filename", help="pass a .txt file to the program", type=str)

    args = parser.parse_args()

    return args


def print_score(user_score, vocab_set, user_incorrect_answers, questions_answered_wrong):
    max_score = len(vocab_set)

    if user_score == max_score:
        print(f"Score: {user_score}/{max_score}.\nYou have no enemies.\n")
    else:
        print(f"Score: {user_score}/{max_score}.\n")
        show_corrections(user_incorrect_answers, questions_answered_wrong, vocab_set)


def show_corrections(user_incorrect_answers, questions_answered_wrong, vocab_set):
    for i in range(len(user_incorrect_answers)):
        print(f"Your translation of {vocab_set[questions_answered_wrong[i]]['kanji']}: {user_incorrect_answers[i]}\nCorrect translation of {vocab_set[questions_answered_wrong[i]]['kanji']}: {vocab_set[questions_answered_wrong[i]]['english']}\n")


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
