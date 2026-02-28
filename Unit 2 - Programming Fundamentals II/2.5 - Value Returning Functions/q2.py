"""
Author: Dinesh Sinnathamby
Date: February 27th, 2026
Description: This program defines a function to check if a number is prime and then uses it in the main function to get user input and display whether the number is prime or not.
"""

def is_prime(num):
    if num < 2:
        return False
    for i in range(2, int(num**0.5) + 1):
        if num % i == 0:
            return False
    return True

def main():
    ongoing = True
    while ongoing:
        num = int(input("Enter a number (or 0 to exit): "))
        if num == 0:
            ongoing = False
        elif is_prime(num):
            print("The number is prime.")
        else:
            print("The number is not prime.")
            
main()