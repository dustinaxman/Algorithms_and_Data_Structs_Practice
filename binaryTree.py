class BinarySearchTree(object):
    def __init__(self,array=[None]):
        self.head=Node(array[0])
        [self.insertValue(i) for i in array[1:]]
    def insertValue(self,val):
        currentNode = self.head
        while True:
            tmpNode = self.descendLevel(currentNode, val)
            if tmpNode is None:
                if currentNode.getValue()>val:
                    return currentNode.setLeft(val)
                else:
                    return currentNode.setRight(val)
            currentNode=tmpNode
    def inOrderTraversal(self):
        return self.traverseLeft([],self.head)
    def traverseLeft(self,array,topNode):
        currentNode = topNode
        nodeStack = [currentNode]
        while not currentNode.getLeft() is None:
            nodeStack.append(currentNode.getLeft())
            currentNode=currentNode.getLeft()
        for tmp in nodeStack[::-1]:
            array.append(tmp)
            if not tmp.getRight() is None:
                self.traverseLeft(array, tmp.getRight())
        return array
    def searchValue(self,val):
        currentNode=self.head
        while True:
            if currentNode is None:
                return False
            elif currentNode.getValue()==val:
                return currentNode.getValue()
            else:
                currentNode=self.descendLevel(currentNode,val)
    def descendLevel(self,currentNode,val):
        newNode=currentNode.getLeft() if currentNode.getValue()>val else currentNode.getRight()
        return newNode

class Node(object):
    def __init__(self,value,leftNode=None,rightNode=None):
        self.value=value
        self.leftNode=leftNode
        self.rightNode=rightNode
    def getValue(self):
        return self.value
    def getRight(self):
        return self.rightNode
    def getLeft(self):
        return self.leftNode
    def setRight(self,val):
        self.rightNode=Node(val)
        return True
    def setLeft(self,val):
        self.leftNode=Node(val)
        return True

b = BinarySearchTree([4,3,7,6,8,5,9,10,2,1,11,4])

print([i.getValue() for i in b.inOrderTraversal()])
b.insertValue(90)
b.insertValue(-5)
b.insertValue(15)
print([i.getValue() for i in b.inOrderTraversal()])
print(b.searchValue(-4))