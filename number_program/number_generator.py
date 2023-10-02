#Built-in imports
import os
import random
import sys


#3rd-party imports
from maskpass import askpass


def main():
    clear_console()

    final_kanji = ""

    sino_num_kanji = {
        "0": "零",
        "1": "一",
        "2": "二",
        "3": "三",
        "4": "四",
        "5": "五",
        "6": "六",
        "7": "七",
        "8": "八",
        "9": "九",
        "10": "十",
        "100": "百",
        "1000": "千",
        "10000": "万"
    }


    selected_num = str(random.randint(0, 99999))

    og_num = selected_num

    digits = count_digits(selected_num)

    while digits > 0:
        if digits != 1:

            first_num = selected_num[:-(int(digits)-1)]

            if first_num != "0":
                if first_num == "1" and digits != 5:
                    final_kanji += sino_num_kanji["1" + ("0" * (int(digits)-1))]
                else:
                    final_kanji += sino_num_kanji[first_num] + sino_num_kanji["1" + ("0" * (int(digits)-1))]

            #Modify the number to remove the digit converted
            selected_num = selected_num [1:]
        else:
            if selected_num != "0":
                final_kanji += sino_num_kanji[selected_num]
        digits -= 1

    print(f"{final_kanji}\n")
    proceed()

    while True:
        user_guess = input("\nWhat is the number in arabic numerals (ie, 3): ")
        if user_guess == og_num:
            print("\nCorrect!")
            proceed()
            break
        else:
            clear_console()
            print(f"{final_kanji}\n")
            print("Incorrect!")


    clear_console()


def proceed():
    choice = askpass("Press enter to continue...", mask="")


def clear_console():
    #Clears the terminal when run
    os.system("clear")


def count_digits(n):
    return len(n)


if __name__ == "__main__":
    main()
