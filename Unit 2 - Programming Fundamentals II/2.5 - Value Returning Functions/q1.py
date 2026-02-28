"""
Author: Dinesh Sinnathamby
Date: February 27th, 2026
Description: This program defines a function to find the maximum of three numbers and then uses it in the main function to get user input and display the result.
"""

def maximum(num1, num2, num3):
    if num1 >= num2 and num1 >= num3:
        return num1
    elif num2 >= num1 and num2 >= num3:
        return num2
    else:
        return num3
    
def main():
    number1 = float(input("Enter the first number: "))
    number2 = float(input("Enter the second number: "))
    number3 = float(input("Enter the third number: "))
    
    max_value = maximum(number1, number2, number3)
    print(f"The maximum value is: {max_value}")