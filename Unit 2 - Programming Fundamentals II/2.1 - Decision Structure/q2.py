"""
Author: Dinesh Sinnathamby
Date: February 19th, 2026
Description: This program demonstrates the use of if-elif-else statements to compare a number to specific values and print corresponding messages.
"""

num1 = int(input("Enter the first number: "))
num2 = int(input("Enter the second number: "))

if num1 % num2 == 0:
    print(num1, "is a multiple of", num2)