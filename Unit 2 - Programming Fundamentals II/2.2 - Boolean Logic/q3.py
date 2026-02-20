"""
Author: Dinesh Sinnathamby
Date: February 20th, 2026
Description: This program prompts the user to enter the number of games purchased, calculates the discount based on the quantity, and then computes the total cost including a 13% tax.
"""

games = int(input("Enter the number of games purchased: "))
if games < 10:
    discount = 0
elif games < 20:
    discount = 0.20
elif games < 50:
    discount = 0.30
elif games < 100:
    discount = 0.40
else:    
    discount = 0.50

total = games * 99 * (1 - discount) * 1.13
print(f"Discount amount: ${games * 99 * discount:.2f}")