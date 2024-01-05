'''
Two Dimensional Array Time Complexity: O(n^2)
'''
import numpy as np

twoDimensionalArr = np.array([[11, 15, 10, 6],
                              [10, 14, 11, 5],
                              [12, 17, 12, 8],
                              [15, 18, 14, 9]])
print(twoDimensionalArr)

def traverseTwoDArr(array):
    for i in range(len(array)):#.................O(mn)
        for j in range(len(array[i])):#..........O(n)
            print(array[i][j])#..................O(1)

traverseTwoDArr(twoDimensionalArr)
