"""
Author: Dinesh Sinnathamby
Date: February 11th, 2026
Description: This program defines a function called 'bmi' that calculates the Body Mass Index (BMI) based on the user's weight and height. The function takes weight and height as parameters, performs the BMI calculation, and prints the result formatted to two decimal places. The main function initializes the user's weight and height and calls the 'bmi' function with these values.
"""

def bmi(weight, height):
    bmi_value = weight / (height ** 2)
    
    print(f"The calculated BMI is: {bmi_value:.2f}")

def main():
    user_weight = 70.0
    user_height = 1.75
    
    bmi(user_weight, user_height)

main()