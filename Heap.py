import random
class Heap(object):
    def __init__(self, array=[None]):
        self.head = array[0]
        if len(array) > 1:
            [self.addElem(i) for i in array[1:]]

    def addElem(self,val):
        currentNode=self.head
        while (not currentNode.getLeft() is None) and (not currentNode.getRight() is None):
            rnd=random.randint(0,1)
            if rnd==0:
                currentNode=currentNode.getRight()
            else:
                currentNode = currentNode.getLeft()
        if not currentNode.getLeft() is None:
            currentNode.setLeft(val)
            child=currentNode.getLeft()
        else:
            currentNode.setRight(val)
            child = currentNode.getRight()
        while currentNode.getValue()>child:
            pass

    def swapValues(self,node1,node2):
        tmp=node1.getValue()
        node1.setValue(node2.getValue)
        node2.setValue(tmp)

    def heapify(self):
        class Node(object):
            def __init__(self, value, leftNode=None, rightNode=None):
                self.value = value
                self.leftNode = leftNode
                self.rightNode = rightNode

            def getValue(self):
                return self.value

            def setValue(self,val):
                self.value=val

            def getRight(self):
                return self.rightNode

            def getLeft(self):
                return self.leftNode

            def setRight(self, val):
                self.rightNode = Node(val)
                return True

            def setLeft(self, val):
                self.leftNode = Node(val)
                return True
