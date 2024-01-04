class Node:

    def __init__(self, data=0, nextNode=None):
        self.data = data
        self.nextNode = nextNode


class LinkedList:

    def __init__(self):
        self.head = None

    def insertStart(self, data):
        node = Node(data, self.head)

if __name__ == '__main__':
    pass