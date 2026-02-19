"""
Author: Dinesh Sinnathamby
Date: February 19th, 2026
Description: This program compares the user's name to the name "Mark" and prints whether the user's name is greater than, equal to, or less than "Mark" based on lexicographical order.
"""

name = input("Enter your name: ")

if name > "Mark":
    print("is greater than Mark" %name)
elif name == "Mark":
    print("Mark is equal to %s" %name)
else:
    print("Mark is greater than %s" %name)