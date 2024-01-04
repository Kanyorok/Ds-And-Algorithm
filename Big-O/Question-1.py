def foo(array):
    sum = 0
    product = 1

    for i in array:
        sum += i

    for i in array:
        product += i
    
    print("Sum = " + str(sum) + ", Product = " + str(product))

# O(n)
# O( A + B)
# The Big-O Notation in this case is O(N)