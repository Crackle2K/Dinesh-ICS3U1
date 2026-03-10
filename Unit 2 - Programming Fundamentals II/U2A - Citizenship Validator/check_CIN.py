"""
Author: Dinesh Sinnathamby
Date: March 9th, 2026
Description: The CIN module file for the citizenship validator assignment made in Python.
"""

def get_digit(number, position):
    if position < 0:
        return 0
    return (number // (10 ** position)) % 10
    # this gets the digit at a position in a number


def digital_root(number):
    return (number // 10) + (number % 10)
    # this gets the sum of the digits

def is_valid(number):
    if number < 0 or number >= 100000000:
        return False

    total = 0

    for pos in range(8):
        digit = get_digit(number, pos)

        if pos % 2 == 1:
            digit = digital_root(digit * 2)

        total += digit

    return total % 10 == 0