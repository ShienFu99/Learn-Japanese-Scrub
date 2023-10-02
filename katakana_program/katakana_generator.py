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

    #Maps each katakana character to its roumaji equivalent
    katakana = [
        {"katakana": "ア", "roumaji": "a"},
        {"katakana": "イ", "roumaji": "i"},
        {"katakana": "ウ", "roumaji": "u"},
        {"katakana": "エ", "roumaji": "e"},
        {"katakana": "オ", "roumaji": "o"},
        {"katakana": "カ", "roumaji": "ka"},
        {"katakana": "キ", "roumaji": "ki"},
        {"katakana": "ク", "roumaji": "ku"},
        {"katakana": "ケ", "roumaji": "ke"},
        {"katakana": "コ", "roumaji": "ko"},
        {"katakana": "サ", "roumaji": "sa"},
        {"katakana": "シ", "roumaji": "shi"},
        {"katakana": "ス", "roumaji": "su"},
        {"katakana": "セ", "roumaji": "se"},
        {"katakana": "ソ", "roumaji": "so"},
        {"katakana": "タ", "roumaji": "ta"},
        {"katakana": "チ", "roumaji": "chi"},
        {"katakana": "ツ", "roumaji": "tsu"},
        {"katakana": "テ", "roumaji": "te"},
        {"katakana": "ト", "roumaji": "to"},
        {"katakana": "ナ", "roumaji": "na"},
        {"katakana": "ニ", "roumaji": "ni"},
        {"katakana": "ヌ", "roumaji": "nu"},
        {"katakana": "ネ", "roumaji": "ne"},
        {"katakana": "ノ", "roumaji": "no"},
        {"katakana": "ハ", "roumaji": "ha"},
        {"katakana": "ヒ", "roumaji": "hi"},
        {"katakana": "フ", "roumaji": "fu"},
        {"katakana": "ヘ", "roumaji": "he"},
        {"katakana": "ホ", "roumaji": "ho"},
        {"katakana": "マ", "roumaji": "ma"},
        {"katakana": "ミ", "roumaji": "mi"},
        {"katakana": "ム", "roumaji": "mu"},
        {"katakana": "メ", "roumaji": "me"},
        {"katakana": "モ", "roumaji": "mo"},
        {"katakana": "ヤ", "roumaji": "ya"},
        {"katakana": "ユ", "roumaji": "yu"},
        {"katakana": "ヨ", "roumaji": "yo"},
        {"katakana": "ラ", "roumaji": "ra"},
        {"katakana": "リ", "roumaji": "ri"},
        {"katakana": "ル", "roumaji": "ru"},
        {"katakana": "レ", "roumaji": "re"},
        {"katakana": "ロ", "roumaji": "ro"},
        {"katakana": "ワ", "roumaji": "wa"},
        {"katakana": "ヲ", "roumaji": "wo"},
        {"katakana": "ン", "roumaji": "n"}
    ]

    #Gets the difficulty level from the user
    difficulty_level = get_difficulty_level()

    #Generates a random string of N (unique) katakana characters -> N is the difficulty_level
    #Also generates the roumaji equivalent
    katakana_str, katakana_str_translation = generate_katakana_str(katakana, difficulty_level)

    #Displays remaining lives
    print(f"\nLives remaining: {user_lives}\n")

    #Displays randomly generated katakana string
    print(katakana_str)

    #Gets the user's translation and evaluates it -> If the user runs out of lives, returns to main
    user_translate(user_lives, katakana_str, katakana_str_translation)

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


def generate_katakana_str(katakana, difficulty_level):
    katakana_str = ""
    katakana_str_translation = ""

    #Runs loop N times -> N = difficulty level
    while difficulty_level != 0:
        difficulty_level -= 1
        #Selects a random katakana character
        katakana_char = choice(katakana)
        #Adds the randomly selected katakana character to the katakana_str + its roumaji equivalent to the translated string
        katakana_str += katakana_char["katakana"]
        katakana_str_translation += katakana_char["roumaji"]
        #Removes the selected katakana character from the list to prevent repeats
        katakana.remove(katakana_char)

    #Returns the hiragan string and its translation to main()
    return (katakana_str, katakana_str_translation)


def user_translate(user_lives, katakana_str, katakana_str_translation):
    user_guesses = []
    guess_count = 0

    print("What is the translation in roumaji?\n")

    #Evalutates user's translation and responds appropriately
    while True:
        #Each guess is saved in a list
        user_guesses.append(input())
        clear_console()

        #If the user's translation is correct, let them know and exit the loop -> ends the program
        if user_guesses[guess_count] == katakana_str_translation:
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
                print(f"{katakana_str}\n")
                print(f"Incorrect! The translation is \"{katakana_str_translation}\".")
                print("\nYour previous guesses:")
                for num, guess in enumerate(user_guesses):
                    print(f"Guess {num+1}: {guess}")
                print()
                break

            #If the user still has remaining lives, let them know their guess is incorrect and display the updated lives counter -> Reprompt for a new guess
            else:
                print("Incorrect! Try again.")
                print(f"Lives remaining: {user_lives}\n")
                print(katakana_str)
                print("\nWhat is the translation in roumaji?\n")


def proceed(prompt):
    #Hides user input + doesn't store it -> Program pauses until the user presses Enter
    getpass(prompt)


def clear_console():
    #Clears the terminal when run
    system("clear")


if __name__ == "__main__":
    main()
