"""
Author: Dinesh Sinnathamby
Date: February 12th, 2026
Description: This program calculates the monthly mortgage payment and the remaining monthly income after the mortgage payment based on user input for the cost of the house, monthly net income, down payment, mortgage interest rate, and monthly maintenance fee.
"""

def display_results(monthlyMortgagePayment, monthlyIncomeRemaining): 
    print("The monthly mortgage payment is %.2f dollars" % monthlyMortgagePayment)
    print("The monthly income remaining is %.2f dollars" % monthlyIncomeRemaining)

def calculate_info(monthlyNetIncome, houseCost, mortageInterestRate, downPayment, monthlyMaintenanceFee):
    PV = houseCost - downPayment
    i = mortageInterestRate / 1200
    monthlyMortgagePayment = (PV * i) / (1 - (1 + i) ** -60) + monthlyMaintenanceFee
    monthlyIncomeRemaining = monthlyNetIncome - monthlyMortgagePayment
    display_results(monthlyMortgagePayment, monthlyIncomeRemaining)
    
def main():
    print("Welcome to the Budget Planning Application.")
    print("Please enter all required information below:")
    houseCost = float(input("%-20s" % "Cost of the property:"))
    monthlyNetIncome = float(input("%-20s" % "Monthly income:"))
    downPayment = float(input("%-20s" % "Down Payment:"))
    mortageInterestRate = float(input("%-20s" % "Mortgage Rate(%):"))
    monthlyMaintenanceFee = float(input("%-20s" % "Maintenance Fee:"))
    calculate_info(monthlyNetIncome, houseCost, mortageInterestRate, downPayment, monthlyMaintenanceFee)

main()