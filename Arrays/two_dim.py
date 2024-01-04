import array as contiguous

# numbers = contiguous.array('I', [[1,2,3,4,5], [8,3,9,12,34]])
numbers = contiguous.array('I', [1,2,3,4,5])
numbers[3] = 89
numbers.insert(6, 87)
# def loopArrays(numVar):
#     for n in range(0, len(numbers)+1):
#         print(n)
       

print(numbers)

print('-_'*30)

'''
Two Dimensional Arrays BootCamp
'''

# Create a two dimensional array to display days and scores
# Day 1 - 11, 15, 10, 6
# Day 2 - 10, 14, 11, 5
# Day 3 - 12, 17, 12, 8
# Day 4 - 15, 18, 14, 9

import numpy as np

twoDimensionalArr = np.array([[11, 15, 10, 6], [10, 14, 11, 5], [12, 17, 12, 8], [15, 18, 14, 9]])

print(twoDimensionalArr)