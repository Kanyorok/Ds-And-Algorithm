def reverse(array):
    for i in range(0, int(len(array)/2)): #...............O(N)
        other = len(array) - i - 1
        temp = array[i]
        array[i] = array[other]
        array[other] = temp
    print(array)

# The Big-O complexity of the code is O(N) [Linear Time].
