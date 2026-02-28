"""
Author: Dinesh Sinnathamby
Date: February 27th, 2026
Description: This program defines a function to convert Fahrenheit to Celsius and then generates a temperature conversion table from 0 to 20 degrees Fahrenheit.
"""

def fahrenheit_to_celsius(fahrenheit):
    celsius = (fahrenheit - 32) * 5 / 9
    return celsius

def temperature_table():
    print("Fahrenheit\tCelsius")
    for fahrenheit in range(0, 21, 1):
        celsius = fahrenheit_to_celsius(fahrenheit)
        print(f"{fahrenheit}\t\t{celsius:.1f}")
        
def main():
    temperature_table()
    
main()