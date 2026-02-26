"""
Author: Dinesh Sinnathamby
Date: February 26th, 2026
Description: This program prompts the user to enter a number between 1 and 10 (inclusive).
"""

num = int(input("Enter a number between 1 and 10 (inclusive): "))
while num < 1 or num > 10:
    print("Invalid input. Please try again.")
    num = int(input("Enter a number between 1 and 10 (inclusive): "))