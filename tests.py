"""
Author: Schuyler Kelly
ID: 3108836
Purpose: Test functions in Assingment 1.
"""

from fizzbuzz import fizzBuzz
import unittest

class TestFizzBuzz(unittest.TestCase):

    # NOTE: "test_" is required for unittest tests functions
    def test_GivenInputIsNotDivisble_by3Or5_thenNoneIsReturned(self):

        # None of the below are divisible by 3 or 5
        self.assertEqual(fizzBuzz(1), None)
        self.assertEqual(fizzBuzz(2), None)
        self.assertEqual(fizzBuzz(4), None)
        self.assertEqual(fizzBuzz(7), None)
        self.assertEqual(fizzBuzz(17), None)
        self.assertEqual(fizzBuzz(101), None)
        self.assertEqual(fizzBuzz(107), None)

    def test_GivenInputIsOnlyDivisible_by3_thenFizzIsReturned(self):

        # All of the below are exclusively divisible by 3
        self.assertEqual(fizzBuzz(21), "Fizz")
        self.assertEqual(fizzBuzz(33), "Fizz")
        self.assertEqual(fizzBuzz(36), "Fizz")
        self.assertEqual(fizzBuzz(51), "Fizz")
        self.assertEqual(fizzBuzz(99), "Fizz")
        self.assertEqual(fizzBuzz(111), "Fizz")
        self.assertEqual(fizzBuzz(123), "Fizz")

    def test_GivenInputIsOnlyDivisible_by5_thenBuzzIsReturned(self):

        # All the the below are exclusively divisible by 5
        self.assertEqual(fizzBuzz(5), "Buzz")
        self.assertEqual(fizzBuzz(40), "Buzz")
        self.assertEqual(fizzBuzz(10), "Buzz")
        self.assertEqual(fizzBuzz(55), "Buzz")
        self.assertEqual(fizzBuzz(110), "Buzz")
        self.assertEqual(fizzBuzz(85), "Buzz")
        self.assertEqual(fizzBuzz(65), "Buzz")

    def test_GivenInputIsDivisble_by3And5_thenFizzBuzzIsReturned(self):
        self.assertEqual(fizzBuzz(15), "FizzBuzz")
        self.assertEqual(fizzBuzz(30), "FizzBuzz")
        self.assertEqual(fizzBuzz(45), "FizzBuzz")
        self.assertEqual(fizzBuzz(60), "FizzBuzz")
        self.assertEqual(fizzBuzz(75), "FizzBuzz")
        self.assertEqual(fizzBuzz(90), "FizzBuzz")
        self.assertEqual(fizzBuzz(105), "FizzBuzz")


if __name__ == "__main__":
    unittest.main()

