import unittest

class Test(unittest.TestCase): # This can be any name!!
    def testcase1(self): # This can be any name!!
        # using self.assertXXXX() write:
        # - assign the value 80 to variable called "a", test that a is equal to 80
        # - assign the value "testing" to variable "b", test that b is not equal to a
        # - assign the array [1,2,3,4] to variable "c" and [2,3,4] to variable "d"
        #       test that c is not equal to d
        # - test that second element of c is equal to first element of d
        # - test that last element of c is equal to last element of d
        # - assign the array [1,2,3,4] to variable "e", test that c is equal to e
        pass
# unittest.main()





def sum(array):
    """
    This function will display the sum of all elements added together.
    Input: array (list) array of numbers
    Output: return the sum of all numbers in array.
    """

    sumValue = 0
    for element in range(1,len(array)+1):
        sumValue += element
    return sumValue


def calculateTax(income):
    """
    This function calculate tax value based on income bracket.
    Those income between 0 and 10,000 will pay 0%
    10,001 - 40,000 will pay 5%
    40,001 - 50,000 will pay 10%
    50,001 - 70,000 will pay 15%
    above 70,000 will pay 20%

    Input: income (int) 
    Output: return the amount of tax needs to be paid
    """

    if income > 0 and income < 10000:
        return 0
    elif income > 10000 and income < 40000:
        return 0.05 * income
    elif income > 40000 and income < 70000:
        return 0.1 * income
    elif income > 70000 and income < 100000:
        return 0.15 * income
    else:
        return 0.2 * income


# with open("output.txt", "w") as file:
#     for i in range(0,100000):
#         if i == 24857 or i == 9848 or i == 12345:
#             continue
#         file.write(str(i))
#         file.write("\n")

import random

with open("output2.txt", "w") as file:
    for i in range(0,99999):
        out = []
        if i == 48563 or i == 28493:
            for i in range(0,6):
                out.append(random.randint(0,100))
        elif i == 193:
            for i in range(0,3):
                out.append(random.randint(101,200))
        elif i == 1928 or i == 93855:
            for i in range(0, 5):
                out.append(random.randint(101,200))
        else:
            for i in range(0,5):
                out.append(random.randint(0,100))
        
        for i in range(0,len(out)):
            file.write(str(out[i]))
            if i == len(out) - 1:
                file.write("\n")
            else:
                file.write(",")
    
        
# print(count)