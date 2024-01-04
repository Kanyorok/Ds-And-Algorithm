'''
  BootCamp Search Example
'''
# Delete the record 89 at index 4 in the array below.
# array marks = [90, 56, 89, 70, 66, 54]
print("My Insertion Example")

import array as arr

arr1 = arr.array('i', [1,2,3,4,5,6,7,8])

def searchArray(array, value):
    for i in array:
        if i == value:
            return array.index(value)
    return "The element does not exist in the array!"

print(f'The value was found at index {searchArray(arr1, 7)}')

print('-'* 50)

'''
TutorialsPoint Insertion Example
'''

def findElement(arr, n, value):
    for i in range(n):
        if arr[i] == value:
            return i
        # if the key is not found
    return -1

# Driver Code
if __name__ == '__main__':
    LA = [1,2,3,4,5,6,7,8]
    print("Array elements are: ")
    for x in range(len(LA)):
        print("LA", [x], " = ", LA[x])
    value = 5
    n = len(LA)
    # Element found using the search operation
    index = findElement(LA, n, value)

    if index != -1:
        print(f'Element {value} was found at position = {str(index + 1)}')
    else:
        print("Element was not found")
        