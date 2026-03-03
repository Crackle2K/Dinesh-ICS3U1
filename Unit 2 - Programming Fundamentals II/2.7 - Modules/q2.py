"""
Author: Dinesh Sinnathamby
Date: March 3rd, 2026
Description: This program calculates the distance between two points in a 2D space.
"""

from math import sqrt, pow

def main():
    xCoord1 = int(input("Enter the x-coordinate of the point: "))
    yCoord1 = int(input("Enter the y-coordinate of the point: "))
    xCoord2 = int(input("Enter the x-coordinate of the second point: "))
    yCoord2 = int(input("Enter the y-coordinate of the second point: "))
    distance = sqrt(pow(xCoord2 - xCoord1, 2) + pow(yCoord2 - yCoord1, 2))

    print("The distance between these two points is", distance, "units.")
    
main()