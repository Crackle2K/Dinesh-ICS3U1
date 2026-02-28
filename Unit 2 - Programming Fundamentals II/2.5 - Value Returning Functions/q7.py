"""
Author: Dinesh Sinnathamby
Date: February 27th, 2026
Description: This program defines a function to convert Fahrenheit to Celsius and then generates a temperature conversion table based on user-defined lower and upper bounds for Fahrenheit values.
"""
    
def fahrenheit_to_celsius(fahrenheit):
    celsius = (fahrenheit - 32) * 5 / 9
    return celsius

def temperature_table(lower_bound, upper_bound):
    print("Fahrenheit\tCelsius")
    for fahrenheit in range(lower_bound, upper_bound + 1):
        celsius = fahrenheit_to_celsius(fahrenheit)
        print(f"{fahrenheit}\t\t{celsius:.1f}")
        
def main():
    lower_bound = int(input("Enter the lower bound of Fahrenheit values: "))
    upper_bound = int(input("Enter the upper bound of Fahrenheit values: "))
    temperature_table(lower_bound, upper_bound)
    
main()