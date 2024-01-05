# Create a two dimensional array to display days and scores
# Day 1 - 11, 15, 10, 6
# Day 2 - 10, 14, 11, 5
# Day 3 - 12, 17, 12, 8
# Day 4 - 15, 18, 14, 9

'''
Two Dimensional Array Time Complexity: O(1)
'''
import numpy as np

twoDimensionalArr = np.array([[11, 15, 10, 6],
                              [10, 14, 11, 5],
                              [12, 17, 12, 8],
                              [15, 18, 14, 9]])
print(twoDimensionalArr)

def accessElements(array, rowIndex, colIndex):
    if rowIndex >= len(array) or colIndex >= len(array[0]):
        print('Incorrect index specified in the input')
    else:
        print(array[rowIndex][colIndex])

accessElements(twoDimensionalArr, 1, 2)
