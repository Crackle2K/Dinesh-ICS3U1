"""
Author: Dinesh Sinnathamby
Date: February 26th, 2026
Description: This program prints a pattern of asterisks in the shape of an inverted triangle followed by a rectangle.
"""

for i in range(6, 0, -1):
    for j in range(i):
        print('*', end=' ')
    print()
print()
for i in range(3):
    for j in range(6):
        print('*', end=' ')
    print() 