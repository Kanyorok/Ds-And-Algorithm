# Write a program to find all pairs of integers whose sum is equal to a given number

'''
My Solution
'''
indices = list()
hashDict = dict()

def twoSum(arr, target):
    for i in range(len(arr)):
        complement = target - arr[i]
        if complement in arr:
            hashDict[complement] = arr.index(complement)


#newArr= [2,6,3,9,11]
newArr = [4, 5, 1, 8]
target = 9
twoSum(newArr, target)
print(sorted(hashDict.values()))

'''
BootCamp Solution
'''
print('*' * 60)
print("Boot Camp solution: ")

def findPairs(nums, target):
    for i in range(len(nums)):
        for j in range(i+1, len(nums)):
            if nums[i] == nums[j]:
                continue
            elif nums[i] + nums[j] == target:
                print(i, j)

findPairs(newArr, target)