"""
Author: Dinesh Sinnathamby
Date: February 26th, 2026
Description: This program prints a multiplication table from 1 to 10.
"""

for i in range(1, 11):
    for j in range(1, 11):
        print(f"{i * j:4}", end="")
    print()
    