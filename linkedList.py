class LinkedList(object):
    def __init__(self, array=[None]):
        self.head = Node(array[0])
        [self.insert(val, i) for i, val in enumerate(array)]

    def insert(self, val, idx):
        currentNode = self.head
        if idx == 0:
            nodeToInsert = Node(val, currentNode)
            self.head = nodeToInsert
        else:
            if not idx == 1:
                for i in range(idx - 1):
                    currentNode = currentNode.getNext()
            nodeToInsert = Node(val, currentNode.getNext())
            currentNode.setNext(nodeToInsert)

    def getElement(self, idx):
        currentNode = self.head
        for i in range(idx):
            currentNode = currentNode.getNext()
        return currentNode

    def findElement(self, val):
        i = 0
        currentNode = self.head
        while not val == currentNode.getValue():
            i += 1
            currentNode = currentNode.getNext()
        return i


class Node(object):
    def __init__(self, value, nextNode=None):
        self.value = value
        self.next = nextNode

    def getValue(self):
        return self.value

    def getNext(self):
        return self.next

    def setNext(self, tmpNode):
        self.next = tmpNode


L = LinkedList([5, 7, 3, 6, 7, 8, 39, 2])
print(L.getElement(4).getValue())
print(L.findElement(39))
print(L.insert(11, 2))
print(L.getElement(2).getValue())
print(L.getElement(3).getValue())
