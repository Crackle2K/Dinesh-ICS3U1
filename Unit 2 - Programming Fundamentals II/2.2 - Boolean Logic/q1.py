"""
Author: Dinesh Sinnathamby
Date: February 20th, 2026
Description: This program prompts the user to enter a number of points and checks if it is valid (between 9 and 51 inclusive).
"""

points = int(input("Enter points: "))
if points < 9 or points > 51:
    print("Invalid points.")
else:
    print("Valid points.")
    