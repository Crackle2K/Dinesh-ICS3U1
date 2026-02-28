"""
Author: Dinesh Sinnathamby
Date: February 27th, 2026
Description: This program defines a function to get user input for first and last names, and then prints them in the format "Last Name, First Name".
"""

import random

def get_inputs():
    first_name = input("Enter your first name: ")
    last_name = input("Enter your last name: ")
    return first_name, last_name

def main():
    first, last = get_inputs()
    print("%s, %s" % (last, first))
    
main()