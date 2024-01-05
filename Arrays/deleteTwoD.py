# Create a two dimensional array to display days and scores
# Day 1 - 11, 15, 10, 6
# Day 2 - 10, 14, 11, 5
# Day 3 - 12, 17, 12, 8
# Day 4 - 15, 18, 14, 9

'''
Two Dimensional Delete Array Column/Row Time Complexity: O(1)
'''
import numpy as np

twoDimensionalArr = np.array([[11, 15, 10, 6],
                              [10, 14, 11, 5],
                              [12, 17, 12, 8],
                              [15, 18, 14, 9]])


newTwoDim = np.insert(twoDimensionalArr, 0, [[1,2,3,4]], axis=1)

print('initial Array')
print(newTwoDim)

print('Array after delete')
newTdArray = np.delete(newTwoDim, 0, axis=1)

print(newTdArray)
