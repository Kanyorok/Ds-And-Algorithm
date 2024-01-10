from lessonlinkdl.linkFramework.node import Node

class dsLinkList(object):
    def __init__(self):
        self.head = None
        self.size = 0
    
    def unShift(self, newFData):
        startData = Node(newFData)
        startData.next = self.head
        self.head = startData
        self.size += 1

    def append(self, newLData):
        if self.head is None:
            self.unShift(newLData)
            return
        
        self.size += 1
        lastData = Node(newLData)
        currentNode = self.head

        while currentNode.next is not None:
            currentNode = currentNode.next
        
        currentNode.next = lastData
    
    def insertAtIndex(self, position, newIdData):
        if pos < 0 or pos > self.size:
            raise IndexError('Index is out of bounds')

        if pos == 0:
            self.unShift(newIdData)

        self.size += 1
        posData = Node(newIdData)
        prevNode = None
        currentNode = self.head
        currentPos = 0

        while currentPos < pos:
            prevNode = currentNode
            currentNode = currentNode.next
            currentPos += 1

        prevNode.next = posData
        posData.next = currentNode

    def delFirst(self):
        self.head = self.head.next 
        self.size -= 1
    
    def pop(self):
        if self.head is None:
            print('List is empty')
        
        currentNode = self.head
        self.size -= 1

        while currentNode.next.next is not None:
            currentNode = currentNode.next
        currentNode.next = None
    
    def delAtIndex(self, index):
        if index < 0 or index > self.size:
            raise IndexError('Cannot delete as it is out of bounds')
        
        if index == 0:
            self.delFirst()
        
        self.size -= 1
        prevNode = None
        currentNode = self.head
        currentPos = 0

        while currentPos < index:
            prevNode = currentNode
            currentNode = currentNode.next
        prevNode.next = currentNode.next

    def printData(self):
        printVals = self.head
        llVals = list()
        while printVals is not None:
            llVals.append(printVals.data)
            printVals = printVals.next
        print(f'The list comprises: {llVals}')
        print(f'The size of list is {self.size}')