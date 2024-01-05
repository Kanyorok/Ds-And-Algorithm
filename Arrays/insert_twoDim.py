# Create a two dimensional array to display days and scores
# Day 1 - 11, 15, 10, 6
# Day 2 - 10, 14, 11, 5
# Day 3 - 12, 17, 12, 8
# Day 4 - 15, 18, 14, 9

import numpy as np

twoDimensionalArr = np.array([[11, 15, 10, 6],
                              [10, 14, 11, 5],
                              [12, 17, 12, 8],
                              [15, 18, 14, 9]])


newTwoDim = np.insert(twoDimensionalArr, 0, [[1,2,3,4]], axis=1)

print(newTwoDim)

print("*.*"*50)

'''
Sample Questionnaire with multiple Options:
'''

print("Which year was world cup recently played?")

mulptiples = np.array([['a.', '2019'],
                       ['b.', '2020'],
                       ['c.', '2021'],
                       ['d.', '2022']])
newMultiples = np.append(mulptiples, [['e.', '2023']], axis=0)
for i in range(len(newMultiples)):
    for j in range(len(newMultiples[i])):
        print("  ",newMultiples[i][j]," ",end="")
    print('\n')
