"""
Author: Dinesh Sinnathamby
Date: February 11th, 2026
Description: This program defines a function called 'birthday' that takes a person's name and age as parameters and prints a birthday message. The function is then called with the name "Dinesh" and age 16.
"""

def birthday(name: str, age: int) -> None:
    print("Happy birthday, " + name + "!")
    print("You are now " + str(age) + " years old.")

birthday("Dinesh", 16)