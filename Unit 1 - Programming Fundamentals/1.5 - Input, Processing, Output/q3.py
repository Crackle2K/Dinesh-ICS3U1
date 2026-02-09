"""
Author: Dinesh Sinnathamby
Date: February 9th, 2026
Description: This program takes the radius of a circle as input and then calculates and outputs the diameter, circumference, and area of the circle."""

radius = float(input("Enter the radius of the circle: "))

print("The diameter of the circle is", str(round(2 * radius, 2)) + '.')
print("The circumference of the circle is", str(round(2 * 3.14159265 * radius, 2)) + '.')
print("The area of the circle is", str(round(3.14159265 * radius ** 2, 2)) + '.')