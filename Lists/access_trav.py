shoppingList = ['Milk', 'Cheese', 'Butter']

print(shoppingList[2])

print('Milk' in shoppingList)


for i in shoppingList:
    print(i)

for i in range(len(shoppingList)):
    shoppingList[i] = shoppingList[i] + "+"
    print(shoppingList[i])
