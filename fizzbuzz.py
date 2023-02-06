"""
Author: Schuyler Kelly
ID: 3108836
Purpose: Write a fizzbuzz method that accepts a number and returns
it as "Fizz" if it's a multiple of 3, "Buzz" if it's a multiple of
5, and "FizzBuzz" if it's a multiple of both.
"""
import sys

"""
Purpose: Reports "Fizz" if multiple of 3, "Buzz" if multiple of 5, and
         "FizzBuzz" if multiple of both.
Parameters:
         num - number being checked against
Returns:
         string representing "Fizz", "Buzz", or "FizzBuzz"
"""
def fizzBuzz(num):
    # Initialize to None so that string will always be returned
    string = None
    if num % 3 == 0:
        string = "Fizz"
    if num % 5 == 0:
        string = "Buzz"
    if num % 3 == 0 and num % 5 == 0:
        string = "FizzBuzz"
    return string

if __name__ == "__main__":
    print(fizzBuzz(int(sys.argv[1])))

