"""
Author: Dinesh Sinnathamby
Date: March 12th, 2026
Description: This program calculates the average of all numerical scores in whatever scores file you set.
"""

def getFile():
     """This function get user input as file name, returns file handler"""
     while(True):
         
        try:
             #read and open file name from user input
             filename = input("Enter a file name: ")
             fileHandler = open(filename, 'r')
             break
         
        except IOError:
             print("File is not found")

     return fileHandler


def main():
    """main logic"""
    total, scores, average, infile = 0, 0, 0, getFile() 
    try:
        #read individual lines from given file
        for line in infile:
            try:
                amount = int(line)
                print (amount)
                total += amount 
                scores +=1
                
            except ValueError: 
                pass
            
        average = total / scores

    except ZeroDivisionError: 
        print("Divide by zero exception") 
    finally:
        print("Don't know")

    infile.close()

    print('Average score: %f' %average)
    print("All Done!")

main()