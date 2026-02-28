"""
Author: Dinesh Sinnathamby
Date: February 27th, 2026
Description: This program defines a function to check if a number is prime and then uses it in the main function to print all prime numbers between 1 and 100.
"""

def is_prime(num):
    if num < 2:
        return False
    for i in range(2, int(num**0.5) + 1):
        if num % i == 0:
            return False
    return True

def main():
    for i in range(1, 100):
        if is_prime(i):
            print(i, end=' ')

main()