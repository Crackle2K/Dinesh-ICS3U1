"""
Author: Dinesh Sinnathamby
Date: February 11th, 2026
Description: This program demonstrates the use of global variables within functions. It defines a global variable 'my_value', a function to display its value, and another function to double its value and display the result.
"""

my_value = 10

def show_value():
    print(my_value)
    
def double_value():
    global my_value
    my_value = my_value * 2
    print(my_value)
    
double_value()
show_value()