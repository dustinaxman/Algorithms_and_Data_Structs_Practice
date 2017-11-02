class Graph(object):
    def __init__(self,array,neighborMat):
        self.nodeList=[]
        self.neighborMat=neighborMat
        [self.nodeList.append(Node(i)) for i in array]
        for idx,node in enumerate(self.nodeList):
            for i,neighborFlag in enumerate(self.neighborMat[idx]):
                if neighborFlag==1:
                    node.addNeighbor(self.nodeList[i])
    def addNode(self,val,neighbors):
        newNode=Node(val,neighbors)
        self.nodeList.append(newNode)
        [self.neighborMat[i].append(1 if (self.nodeList[i] in neighbors) else 0) for i in range(len(self.neighborMat))]
        self.neighborMat.append([(1 if i in neighbors else 0) for i in self.nodeList])
        [node.addNeighbor(newNode) for node in neighbors]
    def breadthFirstSearch(self,startNode,endNode):
        pathQueue=[[startNode]]
        visitedList=[]
        while True:
            tmpPath=pathQueue.pop()
            for i in tmpPath[-1].getNeighbors():
                if not i in visitedList:
                    pathQueue=[tmpPath + [i]]+pathQueue
                    visitedList.append(i)
                if i is endNode:
                    return tmpPath + [i]


    def depthFirstSearch(self,startNode,endNode):
        pathQueue = [[startNode]]
        visitedList = []
        while True:
            tmpPath = pathQueue.pop()
            for i in tmpPath[-1].getNeighbors():
                if not i in visitedList:
                    pathQueue = pathQueue+[tmpPath + [i]]
                    visitedList.append(i)
                if i is endNode:
                    return tmpPath + [i]

    def dijkstra(self,startNode,endNode):
        visitedSet=[]
        visitedSetDistance=[]
        unVisitedSetDistance=[0]
        unVisitedSet=[startNode]  #this would be a heap usually
        currentNode=None
        while True:
            idxOfMin=unVisitedSetDistance.index(min(unVisitedSetDistance))
            currentNode=unVisitedSet[idxOfMin]
            currentNodeDistance=min(unVisitedSetDistance)
            if currentNode is endNode:
                #traceback
                path=[endNode]
                while not currentNode==startNode:
                    currentNode = currentNode.getParent()
                    path.append(currentNode)
                    path.reverse()
                return path
            unVisitedSet.pop(idxOfMin)
            unVisitedSetDistance.pop(idxOfMin)
            visitedSet.append(currentNode)
            visitedSetDistance.append(currentNodeDistance)
            for i in currentNode.getNeighbors():
                if i not in visitedSet:
                    if i in unVisitedSet:
                        if (currentNodeDistance+self.neighborMat[self.nodeList.index(currentNode)][self.nodeList.index(i)])<unVisitedSetDistance[unVisitedSet.index(i)]:
                            unVisitedSetDistance[unVisitedSet.index(i)]=(currentNodeDistance + self.neighborMat[self.nodeList.index(currentNode)][self.nodeList.index(i)])
                            i.setParent(currentNode)
                    else:
                        unVisitedSet.append(i)
                        i.setParent(currentNode)
                        unVisitedSetDistance.append(currentNodeDistance+self.neighborMat[self.nodeList.index(currentNode)][self.nodeList.index(i)])



class Node(object):
    def __init__(self, value, neighbors=None,parent=None):
        if neighbors is None:
            self.neighbors=[]
        else:
            self.neighbors = neighbors

        self.value = value
        self.parent=parent

    def getValue(self):
        return self.value

    def getNeighbors(self):
        return self.neighbors

    def getParent(self):
        return self.parent

    def setParent(self,parent):
        self.parent=parent

    def addNeighbor(self, neighbor):
        self.neighbors.append(neighbor)

    def removeNeighbor(self, neighbor):
        self.neighbors.remove(neighbor)

g=Graph([1,2,3],[[100,1,100],[1,100,1],[100,1,100]])
g.addNode(11,[g.nodeList[i] for i in [0,2]])
print([g.nodeList[0].getNeighbors()[i].getValue() for i in range(len(g.nodeList[0].getNeighbors()))])
print([g.nodeList[1].getNeighbors()[i].getValue() for i in range(len(g.nodeList[1].getNeighbors()))])
print([g.nodeList[2].getNeighbors()[i].getValue() for i in range(len(g.nodeList[2].getNeighbors()))])
print([g.nodeList[3].getNeighbors()[i].getValue() for i in range(len(g.nodeList[3].getNeighbors()))])
print([i.getValue() for i in (g.breadthFirstSearch(g.nodeList[0],g.nodeList[2]))])
print([i.getValue() for i in (g.dijkstra(g.nodeList[0],g.nodeList[2]))])