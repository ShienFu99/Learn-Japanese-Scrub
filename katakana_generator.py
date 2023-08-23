"""
    katakana_generator.py
    Author: ShienFu99
    Date: 8/23/2023
    Description: A program that will lets the user practice reading katakana
    > Generates a random string of katakana (without repeating characters)
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

    katakana = [
        {"katakana": "ア", "romaji": "a"},
        {"katakana": "イ", "romaji": "i"},
        {"katakana": "ウ", "romaji": "u"},
        {"katakana": "エ", "romaji": "e"},
        {"katakana": "オ", "romaji": "o"},
        {"katakana": "カ", "romaji": "ka"},
        {"katakana": "キ", "romaji": "ki"},
        {"katakana": "ク", "romaji": "ku"},
        {"katakana": "ケ", "romaji": "ke"},
        {"katakana": "コ", "romaji": "ko"},
        {"katakana": "サ", "romaji": "sa"},
        {"katakana": "シ", "romaji": "shi"},
        {"katakana": "ス", "romaji": "su"},
        {"katakana": "セ", "romaji": "se"},
        {"katakana": "ソ", "romaji": "so"},
        {"katakana": "タ", "romaji": "ta"},
        {"katakana": "チ", "romaji": "chi"},
        {"katakana": "ツ", "romaji": "tsu"},
        {"katakana": "テ", "romaji": "te"},
        {"katakana": "ト", "romaji": "to"},
        {"katakana": "ナ", "romaji": "na"},
        {"katakana": "ニ", "romaji": "ni"},
        {"katakana": "ヌ", "romaji": "nu"},
        {"katakana": "ネ", "romaji": "ne"},
        {"katakana": "ノ", "romaji": "no"},
        {"katakana": "ハ", "romaji": "ha"},
        {"katakana": "ヒ", "romaji": "hi"},
        {"katakana": "フ", "romaji": "fu"},
        {"katakana": "ヘ", "romaji": "he"},
        {"katakana": "ホ", "romaji": "ho"},
        {"katakana": "マ", "romaji": "ma"},
        {"katakana": "ミ", "romaji": "mi"},
        {"katakana": "ム", "romaji": "mu"},
        {"katakana": "メ", "romaji": "me"},
        {"katakana": "モ", "romaji": "mo"},
        {"katakana": "ヤ", "romaji": "ya"},
        {"katakana": "ユ", "romaji": "yu"},
        {"katakana": "ヨ", "romaji": "yo"},
        {"katakana": "ラ", "romaji": "ra"},
        {"katakana": "リ", "romaji": "ri"},
        {"katakana": "ル", "romaji": "ru"},
        {"katakana": "レ", "romaji": "re"},
        {"katakana": "ロ", "romaji": "ro"},
        {"katakana": "ワ", "romaji": "wa"},
        {"katakana": "ヲ", "romaji": "wo"},
        {"katakana": "ン", "romaji": "n"}
    ]

    user_level = get_user_level()

    random_str, random_str_translation = generate_random_str(katakana, user_level)

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


def generate_random_str(katakana, user_level):
    random_str = ""
    random_str_translation = ""

    while user_level != 0:
        user_level -= 1
        katakana_char = random.choice(katakana)
        random_str += katakana_char["katakana"]
        random_str_translation += katakana_char["romaji"]
        katakana.remove(katakana_char)

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
