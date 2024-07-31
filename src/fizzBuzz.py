"""
This is another puzzle from HackerRank.  The goal is to print the stdout the every number from 1 to the passed
value (n), inclusive of n.  What is required, is to know how to make a loop, when an iterable object is not provided,
to know the math to determine when a number is a factor of another number, and to create a fast method of evaluating
the requirements.
"""

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


if __name__ == '__main__':
    n = 35
    fizzBuzz(n)
