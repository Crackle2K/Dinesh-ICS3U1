"""
Author: Dinesh Sinnathamby
Date: February 26th, 2026
Description: This program calculates the sum of the series 1/10 + 2/9 + 3/8 + ... + 10/1.
"""

sum = 0
for i in range(1, 11):
    sum += i / (11 - i)
print(f"The sum of the series is: {sum:.2f}")