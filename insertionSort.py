def insertSort(array):
    tmpArray=[]
    [insertIntoSortedArray(i,tmpArray) for i in array]
    return tmpArray


def insertIntoSortedArray(val,array):
    if len(array)==0:
        array.append(val)
    else:
        for i,v in enumerate(array):
            if v>val:
                array.insert(i,val)
                break
        else:
            array.append(val)
a=[1,2,4,6,7]
insertIntoSortedArray(5,a)
print(a)
print(insertSort([5,2,7,3,8,5,7,6,1]))