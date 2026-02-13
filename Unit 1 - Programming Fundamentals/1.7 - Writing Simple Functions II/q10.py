"""
Author: Dinesh Sinnathamby
Date: February 11th, 2026
Description: This program defines a function called 'bmi' that calculates the Body Mass Index based on the user's weight and height.
"""

def bmi(weight, height):
    bmi_value = weight / (height ** 2)
    
    print(f"The calculated BMI is: {bmi_value}")

def main():
    user_weight = float(input("Enter your weight in kilograms: "))
    user_height = float(input("Enter your height in meters: "))
    
    bmi(user_weight, user_height)

main()