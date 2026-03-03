"""
Author: Dinesh Sinnathamby
Date: March 3rd, 2026
Description: This program calculates the average of five scores and determines the corresponding letter grade based on the average score.
"""

class grading():
    def calc_average(score1, score2, score3, score4, score5):
        average = (score1 + score2 + score3 + score4 + score5) / 5
        return average
    
    def determine_grade(average):
        if average >= 90:
            return "A"
        elif average >= 80:
            return "B"
        elif average >= 70:
            return "C"
        elif average >= 60:
            return "D"
        else:
            return "F"
        
def main():
    score1 = float(input("Enter the first score: "))
    score2 = float(input("Enter the second score: "))
    score3 = float(input("Enter the third score: "))
    score4 = float(input("Enter the fourth score: "))
    score5 = float(input("Enter the fifth score: "))
    
    average = grading.calc_average(score1, score2, score3, score4, score5)
    grade = grading.determine_grade(average)
    
    print(f"The average score is: {average:.2f}.")
    print(f"The average grade is: {grade}.")
    
main()