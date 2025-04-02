
import math
import unittest


def factorial(n):
    try:
        # Check if input is a valid number
        if not isinstance(n, (int, float)):
            raise ValueError("Error: Input must be a number.")

        # Raise an error for negative values
        if n < 0:
            raise ValueError("Error: Factorial is not defined for negative values.")

        # Raise an error for values greater than 9
        if n > 9:
            raise ValueError("Error: Factorial is not defined for numbers greater than 9.")

        # Compute factorial for positive integers
        if isinstance(n, int) and n >= 0:
            result = math.factorial(n)

        # Compute factorial for floats using the Gamma function#-
        else:
            result = math.gamma(n + 1)

        return result  # Return only the computed result#-

    except ValueError as e:
        return str(e)


# print(factorial(5))
# print(factorial(4))
# print(factorial(3))
# print(factorial(2))
# print(factorial(1))
# print(factorial(0))
# print(factorial(10))
# print(factorial(-1))
# print(factorial("a"))

# The factorial Test Suite


class TestFactorialFunction(unittest.TestCase):

    # Test for positive integers with value and expected result#-
    def test_positive_integer(self):
        self.assertEqual(factorial(5), 120)

    # Test for zero with value and expected result
    def test_zero(self):
        self.assertEqual(factorial(0), 1)

    # Test for negative integers (should raise an error)
    # def test_negative_integer(self):
    #     self.assertEqual(factorial(-3), "Error: Factorial is not defined for negative values.")
    #     self.assertEqual(factorial(-9), "Error: Factorial is not defined for negative values.")

    # # Test for negative floats (should raise an error)
    # def test_negative_float(self):
    #     self.assertEqual(factorial(-3.5), "Error: Factorial is not defined for negative values.")

    # # Test for large negative numbers (should raise an error)
    # def test_large_negative(self):
    #     self.assertEqual(factorial(-10), "Error: Factorial is not defined for negative values.")

    # # Test for large positive numbers (should raise an error)
    # def test_large_positive(self):
    #     self.assertEqual(factorial(10), "Error: Factorial is not defined for numbers greater than 9.")

    # # Test for non-numeric input (string)
    # def test_non_numeric_string(self):
    #     self.assertEqual(factorial("a"), "Error: Input must be a number.")

    # Test for one (edge case)
    def test_one(self):
        self.assertEqual(factorial(1), 1)

    # Test for two (edge case)
    def test_two(self):
        self.assertEqual(factorial(2), 2)

    # THESE ARE TESTS OUTSIDE THE RANGE

    # def testing_wrong_greathan_9(self):
    #     self.assertEqual(factorial(10), 3628800)

    # def testing_wrong_negative(self):
    #     self.assertEqual(factorial(-3), 2)

    # def testing_wrong_string(self):
    #     self.assertEqual(factorial("a"), 10)

    # def testing_wrong_neg_float(self):
    #     self.assertEqual(factorial(-3.2), "Answer")

    # def testing_wrong_float_positive(self):
    #     self.assertEqual(factorial(9.1), 40321.5)


if __name__ == '__main__':
    unittest.main()
# Test for two (edge case)
