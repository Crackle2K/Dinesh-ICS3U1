"""
Author: Dinesh Sinnathamby
Date: March 12th, 2026
Description: This file reads and returns the contents of a requested file, and displays an error message if the file is not found.
"""

fileName = input("Enter a file name: ")

try:
    requestedFile = open(fileName, 'r')
    contents = requestedFile.readlines()
    requestedFile.close()
    
    cycle = 1
    for line in contents:
        print(str(cycle) + ':', line)
        cycle += 1

except IOError:
    print("This file does not exist.")