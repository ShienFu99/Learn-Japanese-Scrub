#Built-in Imports
from getpass import getpass
from os import system
from random import choice
from sys import exit


def main():
    #Hide command that runs the program
    clear_console()

    #User starts with 3 lives
    user_lives = 3

    #Maps each hiragana to its roumaji equivalent
    hiragana = [
        {"hiragana": "あ", "roumaji": "a"},
        {"hiragana": "い", "roumaji": "i"},
        {"hiragana": "う", "roumaji": "u"},
        {"hiragana": "え", "roumaji": "e"},
        {"hiragana": "お", "roumaji": "o"},
        {"hiragana": "か", "roumaji": "ka"},
        {"hiragana": "き", "roumaji": "ki"},
        {"hiragana": "く", "roumaji": "ku"},
        {"hiragana": "け", "roumaji": "ke"},
        {"hiragana": "こ", "roumaji": "ko"},
        {"hiragana": "さ", "roumaji": "sa"},
        {"hiragana": "し", "roumaji": "shi"},
        {"hiragana": "す", "roumaji": "su"},
        {"hiragana": "せ", "roumaji": "se"},
        {"hiragana": "そ", "roumaji": "so"},
        {"hiragana": "た", "roumaji": "ta"},
        {"hiragana": "ち", "roumaji": "chi"},
        {"hiragana": "つ", "roumaji": "tsu"},
        {"hiragana": "て", "roumaji": "te"},
        {"hiragana": "と", "roumaji": "to"},
        {"hiragana": "な", "roumaji": "na"},
        {"hiragana": "に", "roumaji": "ni"},
        {"hiragana": "ぬ", "roumaji": "nu"},
        {"hiragana": "ね", "roumaji": "ne"},
        {"hiragana": "の", "roumaji": "no"},
        {"hiragana": "は", "roumaji": "ha"},
        {"hiragana": "ひ", "roumaji": "hi"},
        {"hiragana": "ふ", "roumaji": "fu"},
        {"hiragana": "へ", "roumaji": "he"},
        {"hiragana": "ほ", "roumaji": "ho"},
        {"hiragana": "ま", "roumaji": "ma"},
        {"hiragana": "み", "roumaji": "mi"},
        {"hiragana": "む", "roumaji": "mu"},
        {"hiragana": "め", "roumaji": "me"},
        {"hiragana": "も", "roumaji": "mo"},
        {"hiragana": "や", "roumaji": "ya"},
        {"hiragana": "ゆ", "roumaji": "yu"},
        {"hiragana": "よ", "roumaji": "yo"},
        {"hiragana": "ら", "roumaji": "ra"},
        {"hiragana": "り", "roumaji": "ri"},
        {"hiragana": "る", "roumaji": "ru"},
        {"hiragana": "れ", "roumaji": "re"},
        {"hiragana": "ろ", "roumaji": "ro"},
        {"hiragana": "わ", "roumaji": "wa"},
        {"hiragana": "を", "roumaji": "wo"},
        {"hiragana": "ん", "roumaji": "n"}
    ]

    #Gets the difficulty level from the user
    difficulty_level = get_difficulty_level()

    #Generates a random string of N (unique) hiragana characters -> N is the difficulty_level
    #Also generates the roumaji equivalent
    hiragana_str, hiragana_str_translation = generate_hiragana_str(hiragana, difficulty_level)

    #Displays remaining lives
    print(f"\nLives remaining: {user_lives}\n")

    #Displays randomly generated hiragana string
    print(hiragana_str)

    #Gets the user's translation and evaluates it -> If the user runs out of lives, returns to main
    user_translate(user_lives, hiragana_str, hiragana_str_translation)

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
        #Adds the randomly selected hiragana character to the hiragana_str + its roumaji equivalent to the translated string
        hiragana_str += hiragana_char["hiragana"]
        hiragana_str_translation += hiragana_char["roumaji"]
        #Removes the selected hiragana character from the list to prevent repeats
        hiragana.remove(hiragana_char)

    #Returns the hiragan string and its translation to main()
    return (hiragana_str, hiragana_str_translation)


def user_translate(user_lives, hiragana_str, hiragana_str_translation):
    user_guesses = []
    guess_count = 0

    print("What is the translation in roumaji?\n")

    #Evalutates user's translation and responds appropriately
    while True:
        #Each guess is saved in a list
        user_guesses.append(input())
        clear_console()

        #If the user's translation is correct, let them know and exit the loop -> ends the program
        if user_guesses[guess_count] == hiragana_str_translation:
            print("Correct!\n")
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
                print(f"Incorrect! The translation is \"{hiragana_str_translation}\".")
                print("\nYour previous guesses:")
                for num, guess in enumerate(user_guesses):
                    print(f"Guess {num+1}: {guess}")
                print()
                break

            #If the user still has remaining lives, let them know their guess is incorrect and display the updated lives counter -> Reprompt for a new guess
            else:
                print("Incorrect! Try again.")
                print(f"Lives remaining: {user_lives}\n")
                print(hiragana_str)
                print("\nWhat is the translation in roumaji?\n")


def proceed(prompt):
    #Hides user input + doesn't store it -> Program pauses until the user presses Enter
    getpass(prompt)


def clear_console():
    #Clears the terminal when run
    system("clear")


if __name__ == "__main__":
    main()
