def mergeSort(array):
    if len(array)==1:
        return array
    else:
        left=array[:len(array)//2]
        right=array[len(array)//2:]
        return orderedCombine(mergeSort(left),mergeSort(right))

def orderedCombine(array1,array2):
    i1=0
    i2=0
    fullArray=[]
    while i1<len(array1) and i2<len(array2):
       if array1[i1]>array2[i2]:
           fullArray.append(array2[i2])
           i2+=1
       elif array1[i1]<array2[i2]:
           fullArray.append(array1[i1])
           i1+=1
       else:
           fullArray=fullArray+[array1[i1],array2[i2]]
           i1+=1
           i2+=1
    if i1==len(array1):
        fullArray=fullArray+array2[i2:]
    elif i2==len(array2):
        fullArray=fullArray + array1[i1:]
    else:
        pass
    return fullArray

print(mergeSort([5,4,5,7,3,2,8,1]))