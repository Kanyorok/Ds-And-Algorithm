def printUnorderedPairs(array):
    for i in range(0, len(array)):
        for j in range(1+1, len(array)):
            print(array[i] + " , " + array[j])

# The Big-O complexity is O(N^2) 