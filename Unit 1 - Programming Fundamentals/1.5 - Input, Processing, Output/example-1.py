"""
Author: Dinesh Sinnathamby
Date: Feburary 9th, 2026
Description: This program takes the user's name and age as input and then outputs a greeting message along with the user's age next year."""

name = input("Enter your name: ")
age = input("Enter your age: ")

print("Hi", name, "how are you? You are", age, "years old.")
print("You are going to be " + str(int(age) + 1), "years old next year.")