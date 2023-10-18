# Program meant to help practice reading / translating hiragana

## Generates N unique hiragana characters for the user to translate into roumaji

* The user must input a difficulty level between 1 and 46 (number of hiragana characters to translate)
* Generates a random string of hiragana (without repeating characters)
* Expects the user to input the translation in roumaji
* The user gets 3 lives before the program shows the correct translation and exits
    -> Displays previous incorrect guesses for review

## How to install / use this program:

This program is run from the command-line and requires Python to run.

1. Click the green "<> Code" button in the github repo and copy the html link
2. Run the following command in a terminal window:
    -> git clone (paste html link here) .
3. Once your in the folder with the .py file, run this command:
    -> python hiragana_generator.py

## Future implementation ideas:

1. Save solution times to a file - compare the current time with the previous fastest

Pseudocode logic:

If there is no previously stored time:
    save the previous time and close the file.
elif there is a previous stored time:
    compare the time and see if it's faster than the previous time:
        if it's faster than the previous time, overwrite it in the file
            -> It took 15.32 seconds to translate the string. Your fastest translation took 10.32s.
        else keep the previous time and close the file.
            -> It took 8.32 seconds to translate the string. New PB!
