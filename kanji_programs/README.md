# Program meant to help improve memorization of kanji word sets

## Reads a file of English words / kanji and prompts the user to translate them (into English or hiragana)

* Expects a .txt or .json file containing a list of words in a dictionary format
    -> Ie: {"kanji": "黄色", "english": "yellow", "kana_reading": "きいろ"}
* Allows the user to select 1 of 3 study methods
    -> English to kana, kanji to English, kanji to kana
* Prompts the user to translate each word into the specified represenation
* Shows the incorrect user translations along with the correct translations

## How to install / use this program:

This program is run from the command-line and requires Python to run.

1. Click the green "<> Code" button in the github repo and copy the html link
2. Run the following command in a terminal window:
    -> git clone (paste html link here) .
    -> Make sure to type the . at the end to copy into the working directory
3. Once your in the folder with the .py file, run this command:
    -> python kanji_practice.py -f *name of file containing the word sets*
    -> Make sure the file containing the word sets is in the working directory as well and ends with .txt or .json
