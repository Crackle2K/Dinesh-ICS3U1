"""
Author: Dinesh Sinnathamby
Date: March 3rd, 2026
Description: This program demonstrates the use of modules in Python. It imports the 'floor' function and 'pi' constant from the 'math' module, but also defines a local function named 'floor' that overrides the imported one. The program then attempts to use the 'floor' function, which will call the local version instead of the one from the 'math' module.
"""

from math import floor, pi

def floor():
    print("Hi")
    
print( floor(4.56) * pi)