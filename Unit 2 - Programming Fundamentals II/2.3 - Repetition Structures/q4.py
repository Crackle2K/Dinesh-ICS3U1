"""
Author: Dinesh Sinnathamby
Date: February 25th, 2026
Description: This program calculates the total pay for a person who is paid one penny on the first day, two pennies on the second day, four pennies on the third day, and so on, doubling the pay each day.
"""

num_days = int(input("Enter the number of days: "))
total_pay = 0
print("Day\tSalary")
for day in range(1, num_days + 1):
    salary = 2 ** (day - 1)
    total_pay += salary
    print(f"{day}\t${salary / 100:.2f}")
print(f"Total pay: ${total_pay / 100:.2f}")