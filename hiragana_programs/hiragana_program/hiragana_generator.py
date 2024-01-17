#Built-in Imports
from getpass import getpass
from os import system
from random import choice
from sys import exit
from time import time


def main():
    #Hide command that runs the program
    clear_console()

    #User starts with 3 lives
    user_lives = 3

    #Maps each hiragana to its rōmaji equivalent
    hiragana = [
        {"hiragana": "あ", "rōmaji": "a"},
        {"hiragana": "い", "rōmaji": "i"},
        {"hiragana": "う", "rōmaji": "u"},
        {"hiragana": "え", "rōmaji": "e"},
        {"hiragana": "お", "rōmaji": "o"},
        {"hiragana": "か", "rōmaji": "ka"},
        {"hiragana": "き", "rōmaji": "ki"},
        {"hiragana": "く", "rōmaji": "ku"},
        {"hiragana": "け", "rōmaji": "ke"},
        {"hiragana": "こ", "rōmaji": "ko"},
        {"hiragana": "さ", "rōmaji": "sa"},
        {"hiragana": "し", "rōmaji": "shi"},
        {"hiragana": "す", "rōmaji": "su"},
        {"hiragana": "せ", "rōmaji": "se"},
        {"hiragana": "そ", "rōmaji": "so"},
        {"hiragana": "た", "rōmaji": "ta"},
        {"hiragana": "ち", "rōmaji": "chi"},
        {"hiragana": "つ", "rōmaji": "tsu"},
        {"hiragana": "て", "rōmaji": "te"},
        {"hiragana": "と", "rōmaji": "to"},
        {"hiragana": "な", "rōmaji": "na"},
        {"hiragana": "に", "rōmaji": "ni"},
        {"hiragana": "ぬ", "rōmaji": "nu"},
        {"hiragana": "ね", "rōmaji": "ne"},
        {"hiragana": "の", "rōmaji": "no"},
        {"hiragana": "は", "rōmaji": "ha"},
        {"hiragana": "ひ", "rōmaji": "hi"},
        {"hiragana": "ふ", "rōmaji": "fu"},
        {"hiragana": "へ", "rōmaji": "he"},
        {"hiragana": "ほ", "rōmaji": "ho"},
        {"hiragana": "ま", "rōmaji": "ma"},
        {"hiragana": "み", "rōmaji": "mi"},
        {"hiragana": "む", "rōmaji": "mu"},
        {"hiragana": "め", "rōmaji": "me"},
        {"hiragana": "も", "rōmaji": "mo"},
        {"hiragana": "や", "rōmaji": "ya"},
        {"hiragana": "ゆ", "rōmaji": "yu"},
        {"hiragana": "よ", "rōmaji": "yo"},
        {"hiragana": "ら", "rōmaji": "ra"},
        {"hiragana": "り", "rōmaji": "ri"},
        {"hiragana": "る", "rōmaji": "ru"},
        {"hiragana": "れ", "rōmaji": "re"},
        {"hiragana": "ろ", "rōmaji": "ro"},
        {"hiragana": "わ", "rōmaji": "wa"},
        {"hiragana": "を", "rōmaji": "wo"},
        {"hiragana": "ん", "rōmaji": "n"}
    ]

    #Gets the difficulty level from the user
    difficulty_level = get_difficulty_level()

    #Generates a random string of N (unique) hiragana characters -> N is the difficulty_level
    #Also generates the rōmaji equivalent
    hiragana_str, hiragana_str_translation = generate_hiragana_str(hiragana, difficulty_level)

    #Displays remaining lives
    print(f"\nLives remaining: {user_lives}\n")

    #Displays randomly generated hiragana string
    print(hiragana_str)

    #Gets the user's translation and evaluates it -> If the user runs out of lives, returns to main
    user_translate(user_lives, hiragana_str, hiragana_str_translation, difficulty_level)

    proceed("Press Enter to exit the program...")
    clear_console()


def get_difficulty_level():
    #Prompts user to input a difficulty level between 1 and 46 (inclusive) -> Reprompts until input is valid, then returns it to main
    while True:
        try:
            difficulty_level = int(input("Set level (between 1 and 46): "))
            if difficulty_level > 46 or difficulty_level < 1:
                raise ValueError
            return difficulty_level
        except ValueError:
            clear_console()
            print("Invalid level! Try again.")


def generate_hiragana_str(hiragana, difficulty_level):
    hiragana_str = ""
    hiragana_str_translation = ""

    #Runs loop N times -> N = difficulty level
    while difficulty_level != 0:
        difficulty_level -= 1
        #Selects a random hiragana character
        hiragana_char = choice(hiragana)
        #Adds the randomly selected hiragana character to the hiragana_str + its rōmaji equivalent to the translated string
        hiragana_str += hiragana_char["hiragana"]
        hiragana_str_translation += hiragana_char["rōmaji"]
        #Removes the selected hiragana character from the list to prevent repeats
        hiragana.remove(hiragana_char)

    #Returns the hiragan string and its translation to main()
    return (hiragana_str, hiragana_str_translation)


def user_translate(user_lives, hiragana_str, hiragana_str_translation, difficulty_level):
    user_guesses = []
    guess_count = 0

    print("What is the translation in rōmaji?\n")

    #Start timer
    start = time()

    #Evalutates user's translation and responds appropriately
    while True:
        #Each guess is saved in a list
        user_guesses.append(input())
        clear_console()

        #If the user's translation is correct, let them know and exit the loop -> ends the program
        if user_guesses[guess_count] == hiragana_str_translation:
            print("Correct!\n")

            #End timer
            end = time()

            #Calculates and pass the new_translation_time to the function for validation
            print(validate_translation_time(f"{end - start:.2f}", difficulty_level))

            #Exits while-loop, returning to main()
            break

        #If the user's translation is wrong...
        else:
            #Decrease lives by 1, guess counter by 1
            user_lives -= 1
            guess_count += 1

            #If the user guesses wrong 3 times in a row, show the proper translation and display their previous guesses -> break out of the loop and end the progam
            if user_lives == 0:
                print(f"{hiragana_str}\n")
                print(f"Incorrect! The correct translation is:\n\"{hiragana_str_translation}\"\n")
                for num, guess in enumerate(user_guesses):
                    print(f"Guess {num+1}: \n\"{guess}\"")
                print()
                break

            #If the user still has remaining lives, let them know their guess is incorrect and display the updated lives counter -> Reprompt for a new guess
            else:
                print("Incorrect! Try again.")
                print(f"Lives remaining: {user_lives}\n")
                print(hiragana_str)
                print("\nWhat is the translation in rōmaji?\n")


#Prompts the user before proceeding with the program
def proceed(prompt):
    #Hides user input + doesn't store it -> Program pauses until the user presses Enter
    getpass(prompt)


#Clears the console
def clear_console():
    #Clears the terminal when run
    system("clear")


#Checks if a file is empty
def file_empty(file):
    #Move file pointer to start of file
    file.seek(0)
    #If the first character of the file cannot be read, return True (file is empty), else False
    if not file.read(1):
        return True
    return False


#Given a file pointer, this function generates its default values
def generate_default_file(file):
    for _ in range(46):
        file.write(f"{_+1}:\"\"\n")


#Compares previous translation_times with the current session's translation_time -> If the user translates N symbols faster than before, records it in a file
#Generates a file if it DNE or its contents are empty
def validate_translation_time(current_translation_time, user_difficulty_level):

    #Creates a list of the previous translation_times stored in the file
    user_translation_times = []

    #If the file is empty or DNE, create the file -> Generate the default values (translation_times = "" means no time has been saved yet)
    with open("translation_times.txt", "a+") as file:
        if file_empty(file):
            generate_default_file(file)

        #Move file pointer to start of the file
        file.seek(0)

        #Read the lines from the file
        lines = file.readlines()

        #Store each line from the file into the list
        for line in lines:
            user_translation_times.append(line.strip())

    #Reopen file in write mode so the previous contents can be overwritten instead of being appended to
    with open("translation_times.txt", "w") as file:
        #The lines in the file span from 1-46 (number of symbols the user chooses to translate) -> Indexing into the list at [user_difficulty-1] returns the line for chosen difficulty_level
        #Split the line to access the previous translation_time for the selected difficulty_level
        file_diff_level, previous_translation_time = user_translation_times[user_difficulty_level-1].split(":", 1)

        #Run this block if the selected difficulty_level has no previously saved translation_time
        #Write the translation_time of the current session into the file for the given difficulty level
        if previous_translation_time == "\"\"":

            user_translation_times[user_difficulty_level-1] = f"{user_difficulty_level}:{current_translation_time}"

            for line in user_translation_times:
                lines = file.write(f"{line}\n")
            return f"Symbols translated in {current_translation_time}s. New PR for {user_difficulty_level}-symbol string!"
        #If a previous translation_time has been saved for the given difficulty level...
        else:
            #Compare the current_translation_time with the previous one to see if the user was faster -> If not, retain the previous file entry
            if current_translation_time > previous_translation_time:
                #The entries in the file span from 1-46, so indexing into the list at the user_diff_level-1 returns the correct entry
                user_translation_times[user_difficulty_level-1] = f"{user_difficulty_level}:{previous_translation_time}"
                for line in user_translation_times:
                    lines = file.write(f"{line}\n")
                return f"Symbols translated in {current_translation_time}s. Previous PR was {previous_translation_time}s."
            #If the user's translation_time is quicker in this session, overwrite the previous translation_time in the file to reflect a new PR
            else:
                #The entries in the file span from 1-46, so indexing into the list at the user_diff_level-1 returns the correct entry
                user_translation_times[user_difficulty_level-1] = f"{user_difficulty_level}:{current_translation_time}"
                for line in user_translation_times:
                    lines = file.write(f"{line}\n")
                return f"Symbols translated in {current_translation_time}s. New PR for {user_difficulty_level}-symbol string!"


if __name__ == "__main__":
    main()
