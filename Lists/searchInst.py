myList = [10, 30, 90, 70, 20]

def searchInList(list, value):
    for i in list:
        if i == value:
            return list.index(value)
    return 'The best outcome in the list'

print(searchInList(myList, 30))