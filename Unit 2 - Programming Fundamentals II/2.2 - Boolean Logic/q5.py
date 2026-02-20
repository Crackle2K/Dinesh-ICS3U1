"""
Author: Dinesh Sinnathamby
Date: February 20th, 2026
Description: This program prompts the user to enter a five-digit integer and checks if it is a palindrome.
"""

number = int(input("Enter a five-digit integer: "))
if number < 10000 or number > 99999:
    print("Invalid input. Please enter a five-digit integer.")
else:
    digit1 = number // 10000
    digit2 = (number // 1000) % 10
    digit3 = (number // 100) % 10
    digit4 = (number // 10) % 10
    digit5 = number % 10

    if digit1 == digit5 and digit2 == digit4:
        print(f"{number} is a palindrome.")
    else:
        print(f"{number} is not a palindrome.")