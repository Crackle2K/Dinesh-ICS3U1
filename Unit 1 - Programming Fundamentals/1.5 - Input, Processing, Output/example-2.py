"""
Author: Dinesh Sinnathamby
Date: February 9th, 2026
Description: This program takes five scores as input, calculates their sum and average, and then outputs the results.
"""


score1 = int(input("Enter the first score: "))
score2 = int(input("Enter the second score: "))
score3 = int(input("Enter the third score: "))
score4 = int(input("Enter the fourth score: "))
score5 = int(input("Enter the fifth score: "))

total = score1 + score2 + score3 + score4 + score5
print("The sum is", total, end=". ")
print("The average is", total / 5)