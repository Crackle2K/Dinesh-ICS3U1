"""
Author: Dinesh Sinnathamby
Date: February 11th, 2026
Description: This program defines a function called 'my_function' that takes three parameters (a, b, c), performs a calculation, and prints the result. The function is then called in the main function using keyword arguments.
"""

def my_function(a, b, c):
    d = (a + c) / b
    print(d)

def main():
    my_function(c=6, a=2, b=4)

main()