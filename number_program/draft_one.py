#Built-in imports
import os
import random
import sys

#3rd-party imports
from maskpass import askpass


def main():
    clear_console()

    while True:
        if len(sys.argv) != 2:
            print("Program launched improperly! Run program with -h or --help for instructions.")
            proceed()
            clear_console()
            sys.exit()

        match sys.argv[1]:
            case "1":
                print("Native or Sino-Japanese?")
                choice = get_choice("Type \"n\" for native Japanese or \"s\" for Sino-Japanese: ", ("n", "s"))
                break
            case "2":
                print(random.randint(0, 99999))
                proceed()
                print("\nReveal kanji...")
                proceed()
                clear_console()
                break
            case "3":
                print("Translate to hiragana or katakana?")
                choice = get_choice("Type \"h\" for hiragana or \"k\" for katakana: ", ("h", "k"))
                break
            case "-h" | "--help":
                clear_console()
                print("Rerun the program with n (where n is a number) to select one of the following options:\n")
                print("1. Translate a Japanese number written in kanji to its arabic numeral form.")
                print("Ie: 四 -> 4\n")
                print("2. Draw the kanji of a number (on paper) written in arabic numeral form.")
                print("Ie: Draw 4 in its kanji form.\n")
                print("3. Translate a Japanese number written in kanji to its hiragana or katakana form.")
                print("Note: This exercise isn't practical for writing out numbers, but it helps practice hiragana and katakana.")
                print("Ie: 四 -> OR 四 ->\n")
                proceed()
                clear_console()
                sys.exit()
            case _:
                sys.exit("Invalid option selected! Run program with -h or --help for instructions.")


def get_choice(prompt, expected_choices):
    while True:
        choice = input(prompt).lower()
        option_1, option_2 = expected_choices

        try:
            if choice != option_1 and choice != option_2:
                raise ValueError
            clear_console()
            return choice
        except ValueError:
            clear_console()


def proceed():
    choice = askpass("Press enter to continue...", mask="")


def clear_console():
    #Clears the terminal when run
    os.system("clear")


if __name__ == "__main__":
    main()
