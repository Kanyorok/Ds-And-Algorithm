def printUnorderedPairs(arrayA, arrayB):
    for i in range(len(arrayA)):
        for j in range(len(arrayB)):
            if arrayA[i] <arrayB[j]:
                print(str(arrayA[i]) + " , " + str(array[j]))

# The Big-O complexity is O(ab) 