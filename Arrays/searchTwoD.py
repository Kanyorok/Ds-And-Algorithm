# Create a two dimensional array to display days and scores
# Day 1 - 11, 15, 10, 6
# Day 2 - 10, 14, 11, 5
# Day 3 - 12, 17, 12, 8
# Day 4 - 15, 18, 14, 9

'''
Two Dimensional Search Array Time Complexity:
```Linear Search=> O(n^2)
```Binary Search=> O(logn)
'''

import numpy as np

twoDimensionalArr = np.array([[11, 15, 10, 6],
                              [10, 14, 11, 5],
                              [12, 17, 12, 8],
                              [15, 18, 14, 9]])
print(twoDimensionalArr)

def searchTwoDArr(array, value):
    for i in range(len(twoDimensionalArr)):
        for j in range(len(array[i])):
            if array[i][j] == value:
                return f'The value is located at the index {str(i)} -- {str(j)}'
    return 'The element was not found'

print(searchTwoDArr(twoDimensionalArr, 14))
