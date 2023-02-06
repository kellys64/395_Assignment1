"""
Author: Schuyler Kelly
ID: 3108836
Purpose: Test functions in Assingment 1.
"""

from fizzbuzz import fizzBuzz
from password_validator import pass_val
import unittest

# NOTE: The print statements are just so that testing is obvious in screenshot

class TestFizzBuzz(unittest.TestCase):

    # NOTE: "test_" is required for unittest tests functions
    def test_GivenInputIsNotDivisble_by3Or5_thenNoneIsReturned(self):

        # None of the below are divisible by 3 or 5
        print()
        print(f"fizzBuzz(1): '{fizzBuzz(1)}' against None")
        self.assertEqual(fizzBuzz(1), None)

        print(f"fizzBuzz(2): '{fizzBuzz(2)}' against None")
        self.assertEqual(fizzBuzz(2), None)

        print(f"fizzBuzz(4): '{fizzBuzz(4)}' against None")
        self.assertEqual(fizzBuzz(4), None)

        print(f"fizzBuzz(7): '{fizzBuzz(7)}' against None")
        self.assertEqual(fizzBuzz(7), None)

        print(f"fizzBuzz(17): '{fizzBuzz(17)}' against None")
        self.assertEqual(fizzBuzz(17), None)

        print(f"fizzBuzz(101): '{fizzBuzz(101)}' against None")
        self.assertEqual(fizzBuzz(101), None)

        print(f"fizzBuzz(107): '{fizzBuzz(107)}' against None")
        self.assertEqual(fizzBuzz(107), None)

    def test_GivenInputIsOnlyDivisible_by3_thenFizzIsReturned(self):

        # All of the below are exclusively divisible by 3
        print()
        print(f"fizzBuzz(21): '{fizzBuzz(21)}' against 'Fizz'")
        self.assertEqual(fizzBuzz(21), "Fizz")

        print(f"fizzBuzz(33): '{fizzBuzz(33)}' against 'Fizz'")
        self.assertEqual(fizzBuzz(33), "Fizz")

        print(f"fizzBuzz(36): '{fizzBuzz(36)}' against 'Fizz'")
        self.assertEqual(fizzBuzz(36), "Fizz")

        print(f"fizzBuzz(51): '{fizzBuzz(51)}' against 'Fizz'")
        self.assertEqual(fizzBuzz(51), "Fizz")

        print(f"fizzBuzz(99): '{fizzBuzz(99)}' against 'Fizz'")
        self.assertEqual(fizzBuzz(99), "Fizz")

        print(f"fizzBuzz(111): '{fizzBuzz(111)}' against 'Fizz'")
        self.assertEqual(fizzBuzz(111), "Fizz")

        print(f"fizzBuzz(123): '{fizzBuzz(123)}' against 'Fizz'")
        self.assertEqual(fizzBuzz(123), "Fizz")

    def test_GivenInputIsOnlyDivisible_by5_thenBuzzIsReturned(self):

        # All the the below are exclusively divisible by 5
        print()
        print(f"fizzBuzz(5): '{fizzBuzz(5)}' against 'Buzz'")
        self.assertEqual(fizzBuzz(5), "Buzz")

        print(f"fizzBuzz(40): '{fizzBuzz(40)}' against 'Buzz'")
        self.assertEqual(fizzBuzz(40), "Buzz")

        print(f"fizzBuzz(10): '{fizzBuzz(10)}' against 'Buzz'")
        self.assertEqual(fizzBuzz(10), "Buzz")

        print(f"fizzBuzz(55): '{fizzBuzz(55)}' against 'Buzz'")
        self.assertEqual(fizzBuzz(55), "Buzz")

        print(f"fizzBuzz(110): '{fizzBuzz(110)}' against 'Buzz'")
        self.assertEqual(fizzBuzz(110), "Buzz")

        print(f"fizzBuzz(85): '{fizzBuzz(85)}' against 'Buzz'")
        self.assertEqual(fizzBuzz(85), "Buzz")

        print(f"fizzBuzz(65): '{fizzBuzz(65)}' against 'Buzz'")
        self.assertEqual(fizzBuzz(65), "Buzz")

    def test_GivenInputIsDivisble_by3And5_thenFizzBuzzIsReturned(self):

        print()
        print(f"fizzBuzz(15): '{fizzBuzz(15)}' against 'FizzBuzz'")
        self.assertEqual(fizzBuzz(15), "FizzBuzz")

        print(f"fizzBuzz(30): '{fizzBuzz(30)}' against 'FizzBuzz'")
        self.assertEqual(fizzBuzz(30), "FizzBuzz")

        print(f"fizzBuzz(45): '{fizzBuzz(45)}' against 'FizzBuzz'")
        self.assertEqual(fizzBuzz(45), "FizzBuzz")

        print(f"fizzBuzz(60): '{fizzBuzz(60)}' against 'FizzBuzz'")
        self.assertEqual(fizzBuzz(60), "FizzBuzz")

        print(f"fizzBuzz(75): '{fizzBuzz(75)}' against 'FizzBuzz'")
        self.assertEqual(fizzBuzz(75), "FizzBuzz")

        print(f"fizzBuzz(90): '{fizzBuzz(90)}' against 'FizzBuzz'")
        self.assertEqual(fizzBuzz(90), "FizzBuzz")

        print(f"fizzBuzz(105): '{fizzBuzz(105)}' against 'FizzBuzz'")
        self.assertEqual(fizzBuzz(105), "FizzBuzz")


class TestPasswordValidator(unittest.TestCase):

    def setUp(self):
        self.lenErr = "Password must be at least 8 characters"
        self.numErr = "Password must contain at least 2 numbers"
        self.capErr = "Password must contain at least one capital"
        self.sChErr = "Password must contain at least one special char"
        self.pass_message = "Password passes!"

    def test_GivenInputIsntLen8_thenReportError(self):

        # Tests should only report the len error

        print()
        print(f"pass_val(\"#He11o\"): '{pass_val('#He11o')}' against '{self.lenErr}'")
        self.assertEqual(pass_val("#He11o"), f"{self.lenErr}")

        # Test for 7 characters
        print(f"pass_val(\"#He11o!\"): '{pass_val('#He11o!')}' against '{self.lenErr}'")
        self.assertEqual(pass_val("#He11o!"), f"{self.lenErr}")

    def test_GivenInputHasNoNum_thenReportError(self):

        # Tests shoulld only report the num error

        print()
        print(f"pass_val(\"#Hello!_\"): '{pass_val('#Hello!_')}' against '{self.numErr}'")
        self.assertEqual(pass_val("#Hello!_"), f"{self.numErr}")

        # Test for one number only
        print(f"pass_val(\"#He1lo!_\"): '{pass_val('#He1lo!_')}' against '{self.numErr}'")
        self.assertEqual(pass_val("#He1lo!_"), f"{self.numErr}")

    def test_GivenInputHasNoCap_thenReportError(self):

        # Tests should only report cap error

        print()
        print(f"pass_val(\"#numb3r5\"): '{pass_val('#numb3r5')}' against '{self.capErr}'")
        self.assertEqual(pass_val("#numb3r5"), f"{self.capErr}")

    def test_GivenInputHasNoSpecialChar_thenReportError(self):

        # Test should only report special character error

        print()
        print(f"pass_val(\"Numb3r5s\"): '{pass_val('Numb3r5s')}' against '{self.sChErr}'")
        self.assertEqual(pass_val("Numb3r5s"), f"{self.sChErr}")

    def test_GivenErrorIsReported_thenErrorsInCorrectOrder(self):

        # Assortment of tests to make sure errors are all reported
        # correctly and in the right order

        print()
        print(f"pass_val(\"hello\"):\n'{pass_val('hello')}'\nagainst\n'{self.lenErr}\n{self.numErr}\n{self.capErr}\n{self.sChErr}'\n")
        self.assertEqual(pass_val("hello"), f"{self.lenErr}\n{self.numErr}\n{self.capErr}\n{self.sChErr}")


        print(f"pass_val(\"He11o\"):\n'{pass_val('He11o')}'\nagainst\n'{self.lenErr}\n{self.sChErr}'\n")
        self.assertEqual(pass_val("He11o"), f"{self.lenErr}\n{self.sChErr}")

        print(f"pass_val(\"#Hello\"):\n'{pass_val('#Hello')}'\nagainst\n'{self.lenErr}\n{self.numErr}'\n")
        self.assertEqual(pass_val("#Hello"), f"{self.lenErr}\n{self.numErr}")

        print(f"pass_val(\"#he11oworld\"):\n'{pass_val('he11oworld')}'\nagainst\n'{self.capErr}\n{self.numErr}'")
        self.assertEqual(pass_val("he11oworld"), f"{self.capErr}\n{self.sChErr}")

    def test_GivenValidPassword_thenReportItPasses(self):

        print()
        print(f"pass_val(\"#This_Wi11_pass!\"): '{pass_val('#This_Will_pass!')}' against '{self.pass_message}'")
        self.assertEqual(pass_val("#This_Wi11_pass!"), f"{self.pass_message}")


if __name__ == "__main__":
    unittest.main()

