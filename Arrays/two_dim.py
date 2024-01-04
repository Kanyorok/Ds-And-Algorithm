import array as contiguous

# numbers = contiguous.array('I', [[1,2,3,4,5], [8,3,9,12,34]])
numbers = contiguous.array('I', [1,2,3,4,5])
numbers[3] = 89
numbers.insert(6, 87)
# def loopArrays(numVar):
#     for n in range(0, len(numbers)+1):
#         print(n)
       

print(numbers)