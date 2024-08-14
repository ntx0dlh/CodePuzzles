"""
This is another puzzle from HackerRank.  The goal is to print the stdout the every number from 1 to the passed
value (n), inclusive of n.  What is required, is to know how to make a loop, when an iterable object is not provided,
to know the math to determine when a number is a factor of another number, and to create a fast method of evaluating
the requirements.
"""
import unittest
import io
import sys

def fizzBuzz(n: int) -> None:
    for i in range(1, n + 1):
        result = str(i)
        # It's important to put the most likely test first, so other tests do not run needlessly.
        # elif is used to prevent further tests if the current test is true.  Also, factors of both 3 & 5 occur the
        # least, but the test must come first, or it will break the logic.  Since 3 & 5 are true, then other tests would
        # also evaluate to true, so this test must come first, or else it will never be reached.
        if i % 3 != 0 and i % 5 != 0:
            pass
        elif i % 3 == 0 and i % 5 == 0:
            result = "FizzBuzz"
        elif i % 3 == 0:
            result = "Fizz"
        elif i % 5 == 0:
            result = "Buzz"
        print(result)


class testFizzBuzz(unittest.TestCase):
    def test_fizzBuzz(self):
        # Capture the output of the function
        captured_output = io.StringIO()
        sys.stdout = captured_output

        # Call the function
        fizzBuzz(15)

        # Restore stdout
        sys.stdout = sys.__stdout__

        # Get the output and split it into lines
        output = captured_output.getvalue().strip().split('\n')

        # Expected output
        expected_output = [
            "1",
            "2",
            "Fizz",
            "4",
            "Buzz",
            "Fizz",
            "7",
            "8",
            "Fizz",
            "Buzz",
            "11",
            "Fizz",
            "13",
            "14",
            "FizzBuzz",
        ]

        # Assert the output
        self.assertEqual(output, expected_output)


if __name__ == '__main__':
    n = 35
    fizzBuzz(n)
    unittest.main()
