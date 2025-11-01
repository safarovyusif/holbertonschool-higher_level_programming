#!/usr/bin/python3
"""
12-roman_to_int.py
Convert a Roman numeral string to an integer (1..3999).
"""


def roman_to_int(roman_string):
    """
    Convert roman_string to its integer value.
    Return 0 if roman_string is not a string or is None.
    """
    if not isinstance(roman_string, str):
        return 0

    values = {'I': 1, 'V': 5, 'X': 10, 'L': 50,
              'C': 100, 'D': 500, 'M': 1000}

    total = 0
    prev_value = 0
    for ch in reversed(roman_string):
        val = values.get(ch, 0)
        if val < prev_value:
            total -= val
        else:
            total += val
            prev_value = val
    return total
