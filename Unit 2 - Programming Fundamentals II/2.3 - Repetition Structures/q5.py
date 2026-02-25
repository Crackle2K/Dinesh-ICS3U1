"""
Author: Dinesh Sinnathamby
Date: February 25th, 2026
Description: This program prompts the user to enter the number of small, medium, and large treats they have.
"""

S = int(input("Enter the number of small treats (0-9): "))
M = int(input("Enter the number of medium treats (0-9): "))
L = int(input("Enter the number of large treats (0-9): "))

if 0 <= S < 10 and 0 <= M < 10 and 0 <= L < 10:
    score = 1 * S + 2 * M + 3 * L
    if score >= 10:
        print("happy")
    else:
        print("sad")
else:
    print("Please enter non-negative integers less than 10.")