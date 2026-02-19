"""
Author: Dinesh Sinnathamby
Date: February 19th, 2026
Description: This program prompts the user to enter a number between 1 and 10 and uses if-elif-else statements to print the corresponding Roman numeral.
"""

number = int(input("Enter a number between 1 and 10: "))

if number == 1:
    print("I")
elif number == 2:
    print("II")
elif number == 3:
    print("III")
elif number == 4:
    print("IV")
elif number == 5:
    print("V")
elif number == 6:
    print("VI")
elif number == 7:
    print("VII")
elif number == 8:
    print("VIII")
elif number == 9:
    print("IX")
elif number == 10:
    print("X")
else:
    print("Invalid input. Please enter a number between 1 and 10.")