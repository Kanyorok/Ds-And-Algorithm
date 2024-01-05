# Concatenation using the '+' operator
a = [1,2,3]
b = [3,8,2]

c = a + b

print(c)

# Multiplication operator

c = a * 8

print(c)

# Inbuilt functions

# size of list
print(len(c))

# max function of list
print(max(c))

# min function in list
print(min(c))

# Total of values in list
print(sum(c))

# Application in calculation find average
print(sum(c)/len(c))

newList = list()
while(True):
    inp = input('Enter a number: ')
    if inp == 'done': break
    value = float(inp)
    newList.append(value)

average = sum(newList) / len(newList)

print(average)