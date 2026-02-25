"""
Author: Dinesh Sinnathamby
Date: February 25th, 2026
Description: This program calculates the calories burned for a person weighing 70 kg while walking at a speed of 5 km/h for different durations.
"""

for minutes in range(5, 65, 5):
    calories_burned = 3.9 * minutes
    print(f"{minutes} minutes: {calories_burned:.2f} calories")