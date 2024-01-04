import array as arr

arr1 = arr.array('i', [1,2,3,4,5,6,7,8])

def accessElement(array, index):
    if index > len(array):
        print('The element is not found in the array!')
    else:
        print(array[index])

accessElement(arr1, 4)
# Time and space complexity is (O(1));