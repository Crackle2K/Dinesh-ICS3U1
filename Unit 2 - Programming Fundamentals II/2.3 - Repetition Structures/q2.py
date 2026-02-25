"""
Author: Dinesh Sinnathamby
Date: February 25th, 2026
Description: This program prompts the user to enter 10 numbers, calculates the total sum and average of those numbers, and then displays the results.
"""

for i in range(10):
    user_input = float(input("Enter a number: "))
    if i == 0:
        total_sum = user_input
    else:
        total_sum += user_input
average = total_sum / 10
print(f"Total sum: {total_sum}")
print(f"Average: {average}")