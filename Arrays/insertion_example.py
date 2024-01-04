'''
  My Insertion Example
'''
# Insert the number 78 at index 4 in the array below.
# array marks = [90, 56, 89, 70, 66, 54]
print("My Insertion Example")
import array as arr

marks = arr.array('i', [90, 56, 89, 70, 66, 54])

print('marks before insertion',marks)

for i in range(0, len(marks)):
    if i == 4:
        marks[i] = 78


print('marks after insertion', marks)
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
