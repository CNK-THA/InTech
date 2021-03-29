import unittest


def sum(array):
    """
    This function will display the sum of all elements added together.
    Input: array (list) array of numbers
    Output: return the sum of all numbers in array.
    """

    sumValue = 0
    for element in range(0,len(array)): 
        sumValue += array[element]
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

    if (income > 0 and income <= 10000) or (income <= 0):
        return 0
    elif income > 10000 and income <= 40000:
        return 0.05 * income
    elif income > 40000 and income <= 50000:
        return 0.1 * income
    elif income > 50000 and income <= 70000:
        return 0.15 * income
    else:
        return 0.2 * income

class Test(unittest.TestCase): # This can be any name!!
    def testcase1(self): # This can be any name!!
        self.assertEquals(sum([1,3,5,7]), 16)
        # self.assertTrue(sum([1,3,5,7]) == 16)
        # self.assertFalse(sum([1,3,5,7]) != 16)

        self.assertEquals(sum([2,4,6,8]), 20)
        self.assertEquals(sum([10,50,30,10]), 100)







        self.assertTrue(calculateTax(5000) == 0)
        self.assertEquals(calculateTax(10000), 0)
        self.assertTrue(calculateTax(17000) == 850)
        self.assertEquals(calculateTax(40000), 2000)
        self.assertEquals(calculateTax(-1000), 0)
        self.assertTrue(calculateTax(0) == 0)
        self.assertTrue(calculateTax(-40000) == 0)


unittest.main()











# with open("output.txt", "w") as file:
#     for i in range(0,100000):
#         if i == 24857 or i == 9848 or i == 12345:
#             continue
#         file.write(str(i))
#         file.write("\n")

# import random

# with open("output2.txt", "w") as file:
#     for i in range(0,99999):
#         out = []
#         if i == 48563 or i == 28493:
#             for i in range(0,6):
#                 out.append(random.randint(0,100))
#         elif i == 193:
#             for i in range(0,3):
#                 out.append(random.randint(101,200))
#         elif i == 1928 or i == 93855:
#             for i in range(0, 5):
#                 out.append(random.randint(101,200))
#         else:
#             for i in range(0,5):
#                 out.append(random.randint(0,100))
        
#         for i in range(0,len(out)):
#             file.write(str(out[i]))
#             if i == len(out) - 1:
#                 file.write("\n")
#             else:
#                 file.write(",")
    
        
# print(count)
