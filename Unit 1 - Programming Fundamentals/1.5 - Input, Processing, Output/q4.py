"""
Author: Dinesh Sinnathamby
Date: February 9th, 2026
Description: This program takes a temperature in Fahrenheit as input, converts it to Celsius, and then outputs the result.
"""

temperature_fahrenheit = float(input("Enter the temperature in Fahrenheit: "))
temperature_celsius = (temperature_fahrenheit - 32) * 5 / 9
print("The temperature in Celsius is", str(round(temperature_celsius, 2)) + '.')