"""
    hiragana_generator.py
    Author: ShienFu99
    Date: 8/22/2023
    Description: A program that will lets the user practice reading hiragana
    > Generates a random string of hiragana (without repeating characters)
    > Expects the user to input the translation in romaji
    > The user gets 3 lives before the program shows the correct translation
"""

#Imports
import random
from maskpass import askpass
import os


def main():
    clear_console()

    user_lives = 3

    hiragana = [
        {"hiragana": "あ", "romaji": "a"},
        {"hiragana": "い", "romaji": "i"},
        {"hiragana": "う", "romaji": "u"},
        {"hiragana": "え", "romaji": "e"},
        {"hiragana": "お", "romaji": "o"},
        {"hiragana": "か", "romaji": "ka"},
        {"hiragana": "き", "romaji": "ki"},
        {"hiragana": "く", "romaji": "ku"},
        {"hiragana": "け", "romaji": "ke"},
        {"hiragana": "こ", "romaji": "ko"},
        {"hiragana": "さ", "romaji": "sa"},
        {"hiragana": "し", "romaji": "shi"},
        {"hiragana": "す", "romaji": "su"},
        {"hiragana": "せ", "romaji": "se"},
        {"hiragana": "そ", "romaji": "so"},
        {"hiragana": "た", "romaji": "ta"},
        {"hiragana": "ち", "romaji": "chi"},
        {"hiragana": "つ", "romaji": "tsu"},
        {"hiragana": "て", "romaji": "te"},
        {"hiragana": "と", "romaji": "to"},
        {"hiragana": "な", "romaji": "na"},
        {"hiragana": "に", "romaji": "ni"},
        {"hiragana": "ぬ", "romaji": "nu"},
        {"hiragana": "ね", "romaji": "ne"},
        {"hiragana": "の", "romaji": "no"},
        {"hiragana": "は", "romaji": "ha"},
        {"hiragana": "ひ", "romaji": "hi"},
        {"hiragana": "ふ", "romaji": "fu"},
        {"hiragana": "へ", "romaji": "he"},
        {"hiragana": "ほ", "romaji": "ho"},
        {"hiragana": "ま", "romaji": "ma"},
        {"hiragana": "み", "romaji": "mi"},
        {"hiragana": "む", "romaji": "mu"},
        {"hiragana": "め", "romaji": "me"},
        {"hiragana": "も", "romaji": "mo"},
        {"hiragana": "や", "romaji": "ya"},
        {"hiragana": "ゆ", "romaji": "yu"},
        {"hiragana": "よ", "romaji": "yo"},
        {"hiragana": "ら", "romaji": "ra"},
        {"hiragana": "り", "romaji": "ri"},
        {"hiragana": "る", "romaji": "ru"},
        {"hiragana": "れ", "romaji": "re"},
        {"hiragana": "ろ", "romaji": "ro"},
        {"hiragana": "わ", "romaji": "wa"},
        {"hiragana": "を", "romaji": "wo"},
        {"hiragana": "ん", "romaji": "n"}
    ]

    user_level = get_user_level()

    random_str, random_str_translation = generate_random_str(hiragana, user_level)

    print(f"\nLives remaining: {user_lives}\n")

    print(random_str)

    user_translate(user_lives, random_str, random_str_translation)

    proceed()

    clear_console()


def get_user_level():
    while True:
        try:
            user_level = int(input("Set level (between 1 and 46): "))
            if user_level > 46 or user_level < 1:
                raise ValueError
            return user_level
        except ValueError:
            clear_console()
            print("Invalid level! Try again.")


def generate_random_str(hiragana, user_level):
    random_str = ""
    random_str_translation = ""

    while user_level != 0:
        user_level -= 1
        hiragana_char = random.choice(hiragana)
        random_str += hiragana_char["hiragana"]
        random_str_translation += hiragana_char["romaji"]
        hiragana.remove(hiragana_char)

    return (random_str, random_str_translation)


def user_translate(user_lives, random_str, random_str_translation):

    print("What is the translation in romaji?\n")

    while True:
        user_romaji = input()
        if user_romaji == random_str_translation:
            clear_console()
            print("Correct!\n")
            break
        else:
            user_lives -= 1
            if user_lives == 0:
                clear_console()
                print(f"{random_str}\n")
                print(f"Incorrect! The translation is \"{random_str_translation}\".")
                break
            else:
                clear_console()
                print("Incorrect! Try again.")
                print(f"Lives remaining: {user_lives}\n")
                print(random_str)
                print("\nWhat is the translation in romaji?\n")
                continue


def proceed():
    choice = askpass("Press enter to continue...", mask="")


def clear_console():
    #Clears the terminal when run
    os.system("clear")


if __name__ == "__main__":
    main()
