"""
Author: Dinesh Sinnathamby
Date: February 27th, 2026
Description: This program defines a function that simulates a fortune teller by generating a random number and returning a corresponding fortune message.
"""

import random

def fortune():
    num = random.randint(1, 5)
    if num == 1:
        return "You will have a great day!"
    elif num == 2:
        return "You will find something valuable."
    elif num == 3:
        return "You will meet someone interesting."
    elif num == 4:
        return "You will achieve your goals."
    else:
        return "You will have a surprise!"
    
def main():
    print(fortune())
    
main()