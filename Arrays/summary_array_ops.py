'''
All Array Operations
'''
import array as arr

# 1. Create an array and traverse
print('Create an array and traverse')
my_array = arr.array('i', [1,2,3,4,5,6])

for i in my_array:
    print (i)

print('`'*50)

print('`'*50)
# 2. Access individual elements through indexes
print('Access individual elements through indexes')

print(f'the first element is { my_array[0]}')

print('`'*50)

print('`'*50)
# 3. Append new element at the end of array
print('Append new element at the end of array')

value = 72
my_array.append(value)
print(f'append {value} at the end of array {my_array}')

print('`'*50)

print('`'*50)
# 4. Insert new element in array using insert() method
print('Insert new element in array using insert() method')

value = 68
index = 3
my_array.insert(index, value)

print(f'Insert {value} at index {index} the final outcome is {my_array}')

print('`'*50)

print('`'*50)
# 5. Extend the size of the array extend() method
print('Extend the size of the array extend() method')

my_array1 = arr.array('i', [10,11,12])
my_array.extend(my_array1)

print(f'The {my_array1} was used to extend original my_array {my_array}')

print('`'*50)

print('`'*50)
# 6. Add items from list into array using fromlist() method  
print('Add items from list into array using fromlist() method')

tmpList = [20, 31, 23, 89]
my_array.fromlist(tmpList)

print(my_array)

print('`'*50)

print('`'*50)
# 7. Remove items from array using remove() method  
print('Remove items from array using remove() method')

my_array.remove(89)
print(my_array)

print('`'*50)

print('`'*50)
# 8. Remove last element using pop() method  
print('Remove last element using pop() method')

my_array.pop()
print(my_array)

print('`'*50)

print('`'*50)

# 9. Fetch any element using the index method
print('Fetch any element using the index method')

print(my_array.index(68))

print('`'*50)

print('`'*50)

# 10. Reverse the elements in an array using the reverse method
print('Reverse the elements in an array using the reverse method')

my_array.reverse()
print(my_array)

print('`'*50)

print('`'*50)

# 11. Get array buffer information using the buffer_info() method
print('Get array buffer information using the buffer_info() method')

print(my_array.buffer_info())
print(my_array)

print('`'*50)

print('`'*50)

# 12. Get array element count using the count() method
print('Get array element count using the count() method')

print(my_array.count(11))

print('`'*50)

print('`'*50)

# 13. Convert array to list using the tolist() method
print('Convert array to list using the tolist() method')

lstTemp = my_array.tolist()

print(lstTemp)

print('`'*50)

print('`'*50)

# 14. Slice elements in an array
print('Slice elements in an array')

print(my_array[2:5])






