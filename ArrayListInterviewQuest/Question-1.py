# Write a program to find the missing number in an array or list
# Find the missing number in an integer array of 1 to 100.
'''
My Solution
'''
import array as arr

def findMissingNum(array):
    # sort the array values
    sortedArr = sorted(array)
    missingVals= arr.array('i')
    
    # check that the values i array are between 1 to 100
    if sortedArr[len(sortedArr) -1] > 100 or sortedArr[0] < 1:
        raise ValueError("The values are above the accepted the range!")

    # traverse through the values
    for i in range(len(sortedArr)-1):
        if sortedArr[i + 1] != sortedArr[i] + 1:
            for j in range(sortedArr[i] + 1, sortedArr[i + 1]):
                missingVals.append(j)
    
    return missingVals


checkArr = arr.array('i', [78, 5, 23, 90, 12, 3, 2, 1, 67])
print(f'Missing values in array: {findMissingNum(checkArr)}')
print(f'The original array: {sorted(checkArr)}')

'''
Bootcamp 
'''
mylist = [1, 2, 3, 4, 5, 6, 7, 8, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36, 37, 38, 39, 40, 41, 42, 43, 44, 45, 46, 47, 48, 49, 50, 51, 52, 53, 54, 55, 56, 57, 58, 59, 60, 61, 62, 63, 64, 65, 66, 67, 68, 69, 70, 71, 72, 73, 74, 75, 76, 77, 78, 79, 80, 81, 82, 83, 84, 85, 86, 87, 88, 89, 90, 91, 92, 93, 94, 95, 96, 97, 98, 99, 100]


def checkMissing(list, n):
    sum1 = 100*101 /2
    sum2 = sum(list)
    print(sum1-sum2)

print('*'* 80)
checkMissing(mylist, 100)
