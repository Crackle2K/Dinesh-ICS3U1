"""
Author: Dinesh Sinnathamby
Date: February 19th, 2026
Description: This program prompts the user to enter the dimensions of two rectangles, calculates their areas, and compares them to determine which rectangle has a greater area or if they are equal.
"""

rect1length = float(input("Enter the length of the first rectangle: "))
rect1width = float(input("Enter the width of the first rectangle: "))
rect2length = float(input("Enter the length of the second rectangle: "))
rect2width = float(input("Enter the width of the second rectangle: "))

if rect1length * rect1width > rect2length * rect2width:
    print("The first rectangle has a greater area than the second rectangle.")
elif rect1length * rect1width < rect2length * rect2width:
    print("The second rectangle has a greater area than the first rectangle.")
else:
    print("The two rectangles have the same area.")