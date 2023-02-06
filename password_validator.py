"""
Author: Schuyler Kelly
ID: 3108836
Purpose: Validates a password using a string input by the user.
"""

import sys
from string import ascii_uppercase, punctuation


"""
Purpose: Creates the error message for the password if it doesn't
         meet requirements.
Parameters:
         string - string passed to pass_val
         num_count - amount of numbers in string
         cap_found - Boolean representing if capital is found
         special_character_found - Boolean representing if special char found
Returns:
         error string
"""
def err_constructor(string, num_count, cap_found, special_character_found):
    string_err = ""

    if len(string) < 8:
        string_err += "Password must be at least 8 characters\n"

    # Finish creating error string depending on results
    if num_count < 2:
        string_err += "Password must contain at least 2 numbers\n"
    if not cap_found:
        string_err += "Password must contain at least one capital\n"
    if not special_character_found:
        string_err += "Password must contain at least one special char\n"

    # Strip extra newline characters
    string_err = string_err.strip()
    return string_err


"""
Purpose: Check if a string is a valid password. Needs 8 length, 2 nums,
         one capital, and one special character.
Parameters:
         string - password being checked
Returns:
         string displaying whether password fails or passes, and why.
"""
def pass_val(string):
    string_err = ""
    num_count = 0
    cap_found = False
    special_character_found = False

    # Iterate over password and check for numbers, capital letters,
    # And special characters
    for character in string:
        if character.isdigit():
            num_count += 1
        if character in ascii_uppercase:
            cap_found = True
        if character in punctuation:
            special_character_found = True

    string_err = err_constructor(string, num_count, cap_found, special_character_found)
    if string_err:
        return string_err
    else:
        return "Password passes!"


if __name__ == "__main__":
    pass_val(sys.argv[1])

