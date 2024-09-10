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

# Taking input from the user
num = input('Please enter a number: ')

# Input validation
try:
    # Convert input to integer
    num = int(num)
    
    # Call the function and print the result
    result = sum_of_digits(num)
    print("Sum of the individual integer digits: ", result)
except ValueError:
    print("Invalid input! Please enter a valid integer.")