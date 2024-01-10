'''
Linked List Data Structure
'''
class Node:
    def __init__(self, data=None):
        self.data = data
        self.next = None

class linkedList:
    def __init__(self):
        self.head = None
        self.size = 0

    def insertStart(self, newSInfo):
        infoStartObject = Node(newSInfo)
        infoStartObject.next = self.head
        self.head = infoStartObject

        self.size += 1
    
    def append(self, newEInfo):
        if self.head == None:
            self.insertStart(newEInfo)
            return
        
        self.size += 1
        infoEndObject = Node(newEInfo)
        actualNode = self.head

        while actualNode.next is not None:
            actualNode = actualNode.next
        
        actualNode.next = infoEndObject

    def insertAtIndex(self, index, newIdData):
        if index < 0 or index > self.size:
            raise IndexError(f'Index: {index} is out of bounds!')

        if index == 0:
            self.infoStartObject(newIdData)

        self.size += 1
        indexInfo = Node(newIdData)
        prevNode = None
        actualNode = self.head
        currentPosition = 0

        while currentPosition < index:
            prevNode = actualNode
            actualNode = actualNode.next
            currentPosition += 1
        
        prevNode.next = indexInfo
        indexInfo.next = actualNode

    def pop(self):
        if index < 0 or index > self.size:
            raise IndexError(f'Index: {index} cannot be removed as it is out of bounds')

        currentData = self.head
        while currentData.next is not None:
            
            currentData = currentData.next

    def printData(self):
        printValues = self.head
        print("Linked List Data: ")
        dataInfo = list()
        while printValues is not None:
            dataInfo.append(printValues.data)
            printValues = printValues.next
        print(dataInfo)
        print(f'The size of data is {self.size}')

ll = linkedList()
ll.insertStart(90)
ll.insertStart("34")
ll.insertStart("Joshua")
ll.insertAtIndex(2, "Kimani")
ll.append("James")
ll.printData()
