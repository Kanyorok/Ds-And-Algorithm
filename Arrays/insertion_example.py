'''
  My Insertion Example
'''
# Insert the number 78 at index 4 in the array below.
# array marks = [90, 56, 89, 70, 66, 54]
print("My Insertion Example")
import array as arr

marks = arr.array('i', [90, 56, 89, 70, 66, 54])
inserted_arr = arr.array('i')

print('marks before insertion',marks)

temp = 0
n = len(marks)

for i in range(0, n):
    if i == 4:
        temp = marks[i]
        marks[i] = 78
        marks[i+1] = temp
    inserted_arr.append(marks[i])


print('marks after insertion', inserted_arr)
print('-'* 50)


'''
TutorialsPoint Insertion Example
'''

# Python program to insert an element using insertion operation
print("TutorialsPoint Insertion Example")
def insert(arr, element):
    arr.append(element)

# Driver Code
if __name__ == '__main__':
    # Step 1: Declare array and value to insert
    LA = [0, 0, 0]
    x = 0
    # Print array before insertion
    print("Print array before insertion")
    for x in range(len(LA)):
        print("LA", [x], " = ", LA[x])
    print("Inserting elements.....") 
    # Array after inserting elements
    for x in range(len(LA)):
        LA.append(x)
        LA[x] = x + 1
    print("Print array after insertion")
    for x in range(len(LA)):
        print("LA", [x], " = ", LA[x])
print('-'* 50)


'''
Insertion Example using Inbuilt Functions
'''

# Python program to insert an element using insertion operation
print("Insertion Example using Inbuilt function")
marks = arr.array('i', [90, 56, 89, 70, 66, 54])
print("Marks before insertion", marks)
marks.insert(5, 78)
print('Inserted 78 at index 5', marks)

# Time Complexity ---> O(n)