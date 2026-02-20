"""
Author: Dinesh Sinnathamby
Date: February 20th, 2026
Description: This program prompts the user to enter a speed and checks if it is valid (between 0 and 200 inclusive).
"""

speed = int(input("Enter speed: "))
if speed < 0 or speed > 200:
    print("Invalid Speed.")
else:
    print("Valid Speed.")