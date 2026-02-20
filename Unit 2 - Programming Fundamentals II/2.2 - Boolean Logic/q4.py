"""
Author: Dinesh Sinnathamby
Date: February 20th, 2026
Description: This program calculates the Body Mass Index (BMI) based on user input for weight and height, and then categorizes the BMI into underweight, optimal weight, overweight, or obese.
"""

def bmi(weight, height):
    bmi_value = weight / (height ** 2)
    
    print(f"The calculated BMI is: {bmi_value}")
    if bmi_value < 18.5:
        print("You are underweight.")
    elif 18.5 <= bmi_value <= 24.9:
        print("You have an optimal weight.")
    elif 25 <= bmi_value <= 29.9:
        print("You are overweight.")
    else:
        print("You are obese.")

def main():
    user_weight = float(input("Enter your weight in kilograms: "))
    user_height = float(input("Enter your height in meters: "))
    
    bmi(user_weight, user_height)

main()

