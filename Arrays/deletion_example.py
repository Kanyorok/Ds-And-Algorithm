'''
  My Deletion Example
'''
# Delete the record 89 at index 4 in the array below.
# array marks = [90, 56, 89, 70, 66, 54]
print("My Insertion Example")
import array as arr

marks = arr.array('i', [90, 56, 89, 70, 66, 54])

print('marks before insertion',marks)

temp = 0
n = len(marks)
del_arr = arr.array('i')

for i in range(0, n-1):
    if marks[i] == 90:
        temp = marks[i]
        marks[i] = marks[i + 1]
        marks[i + 1] = temp
    del_arr.append(marks[i])

print('marks after deletion', del_arr)
print('-'* 50)

'''
TutorialsPoint Insertion Example
'''

# Python program to insert an element using insertion operation
print("TutorialsPoint Insertion Example")

if __name__ == '__main__':
    # Declaring array and deleting the value
    LA = [0,0,0,0]
    n = len(LA)

    print("Array Before Deletion: ")
    for x in range(n):
        LA[x] = x + 3
        print("LA", [x], " = ", LA[x])
    # delete the value if it exists
    # or show error if it does not exist in list

    for x in range(1, n-1):
        LA[x] = LA[x + 1]
        n = n - 1
    print("Array after deletion of last element: ")
    for x in range(n):
        print("LA", [x], " = ", LA[x])