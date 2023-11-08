#!/usr/bin/python3
def roman_to_int(roman_string):
    # Check if the input is a string
    if not isinstance(roman_string, str) or roman_string is None:
        return 0

    # Define the Roman numerals and their integer value
    roman_numerals = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000}

    # Initialize the previous value and total
    prev_value = 0
    total = 0

    # Iterate over each character in the Roman numeral string
    for numeral in reversed(roman_string):
        # Convert the Roman numeral to an integer
        value = roman_numerals.get(numeral, 0)

        # If the numeral is smaller than the previous one, subtract it
        if value < prev_value:
            total -= value
        else:
            # Otherwise, add it and update the previous value
            total += value
            prev_value = value

    return total
