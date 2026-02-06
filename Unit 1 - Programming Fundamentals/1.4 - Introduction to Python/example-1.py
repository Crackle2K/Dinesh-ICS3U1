"""
Author: Dinesh Sinnathamby
Date: Feburary 6th, 2026
Description: This program demonstrates the use of operators and keywords in Python. It shows how to use the + operator to concatenate strings and add integers, and it also lists all the keywords in Python using the keyword module.
"""

import keyword

print("1" + 1)  # <-- This will raise a TypeError because you cannot concatenate a string and an integer.
print("1" + "1")  # <-- This will print "11" because both operands are strings and can be concatenated together.
print(1 + 1)  # <-- This will print 2 because both operands are integers and can be added together.

keywords = keyword.kwlist
for word in keywords:
    print(word)
    
print("End")