import unittest

def sum_of_digits(n: int) -> int:
    """
    Function to calculate the sum of the individual digits of a given integer.
    
    Parameters:
    n (int): The input integer whose digits' sum is to be calculated.
    
    Returns:
    int: Sum of the digits of the integer.
    """

    # Ensure that we work with the absolute value to handle negative numbers
    n = abs(n)
    
    # Convert the number to a string, iterate over each character, convert to integer and sum them up
    return sum(int(digit) for digit in str(n))


class TestSumOfDigits(unittest.TestCase):
    def test_positive_number(self):
        self.assertEqual(sum_of_digits(123), 6, "Test case failed for input 123")

    def test_negative_number(self):
        self.assertEqual(sum_of_digits(-456), 15, "Test case failed for input -456")

    def test_zero(self):
        self.assertEqual(sum_of_digits(0), 0, "Test case failed for input 0")

    def test_single_digit(self):
        self.assertEqual(sum_of_digits(7), 7, "Test case failed for input 7")

    def test_large_number(self):
        self.assertEqual(sum_of_digits(987654321), 45, "Test case failed for input 987654321")

    def test_repeated_digits(self):
        self.assertEqual(sum_of_digits(1111), 4, "Test case failed for input 1111")
        
    def test_mixed_digits(self):
        self.assertEqual(sum_of_digits(120304), 10, "Test case failed for input 120304")


if __name__ == "__main__":
    unittest.main()