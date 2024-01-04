def powerNum(base, exp):
    assert exp >=0 and int(exp) == exp, 'The number must be a positive integer only'
    if exp == 0:
        return 1
    if exp == 1:
        return base        
    return base * powerNum(base, exp-1)

print(powerNum(4.7,2))