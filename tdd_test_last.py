
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


print(factorial(5))
print(factorial(4))
print(factorial(3))
print(factorial(2))
print(factorial(1))
print(factorial(0))
print(factorial(10))
print(factorial(-1))
print(factorial("a"))
