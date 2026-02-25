"""
Author: Dinesh Sinnathamby
Date: February 25th, 2026
Description: This program uses a for loop to print the multiples of -11 from -11 to -99, separated by commas.
"""

for i in range(-11, -100, -11):
    if i == -99:
        print(i)
    else:
        print(i, end=', ')