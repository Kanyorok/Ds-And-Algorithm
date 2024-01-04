def decimalToBinary(n):
    assert int(n) == n, 'The number should be a positive integer'
    if (n == 0):
        return 0
    else:
        return n%2 + 10 * decimalToBinary(n//2)

print(decimalToBinary(9))

