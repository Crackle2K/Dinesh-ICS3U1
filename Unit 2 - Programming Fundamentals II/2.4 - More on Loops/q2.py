"""
Author: Dinesh Sinnathamby
Date: February 26th, 2026
Description: This program prompts the user to enter positive numbers and keeps track of the highest and lowest numbers entered. The program stops when the user enters a negative number.
"""

highest = 0
lowest = 9999999999999999999999999999999999999999999999999

while True:
    num = int(input("Enter a positive number (or a negative number to stop): "))
    if num < 0:
        break
    else:
        if num > highest:
            highest = num
        elif num < lowest:
            lowest = num

print("The highest number entered is:", highest)
print("The lowest number entered is:", lowest)