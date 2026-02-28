"""
Author: Dinesh Sinnathamby
Date: February 27th, 2026
Description: This program defines a function to simulate a coin toss and returns either "Heads" or "Tails".
"""

import random

def toss():
    if random.randint(1, 2) == 1:
        return "Heads"
    else:
        return "Tails"
    
def main():
    result = toss()
    print(f"The result of the coin toss is: {result}")
    
main()