"""
Author: Dinesh Sinnathamby
Date: February 11th, 2026
Description: This program defines a function called 'show_data' that takes a person's name and age as parameters and prints a message.
"""

def show_data(name, age):
    print("Hello", name, "you are", age, "years old!")
    
def main():
    show_data("Dinesh", 15)
    show_data(age=15, name="Dinesh")

main()