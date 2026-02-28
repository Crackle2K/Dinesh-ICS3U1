"""
Author: Dinesh Sinnathamby
Date: February 27th, 2026
Description: This program defines a function to simulate rolling a six-sided die 1000 times and counts how many times each face appears.
"""

import random

def roll_die():
    count1, count2, count3, count4, count5, count6 = 0, 0, 0, 0, 0, 0
    for i in range(1, 1001):
        roll = random.randint(1, 6)
        if roll == 1:
            count1 += 1
        elif roll == 2:
            count2 += 1
        elif roll == 3:
            count3 += 1
        elif roll == 4:
            count4 += 1
        elif roll == 5:
            count5 += 1
        else:
            count6 += 1
    return count1, count2, count3, count4, count5, count6

def main():
    count1, count2, count3, count4, count5, count6 = roll_die()
    print(f"Number of times 1 was rolled: {count1}")
    print(f"Number of times 2 was rolled: {count2}")
    print(f"Number of times 3 was rolled: {count3}")
    print(f"Number of times 4 was rolled: {count4}")
    print(f"Number of times 5 was rolled: {count5}")
    print(f"Number of times 6 was rolled: {count6}")

main()