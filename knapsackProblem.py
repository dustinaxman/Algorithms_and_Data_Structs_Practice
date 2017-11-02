def bestItemChoice(B,S,bagSize):
    allItems=[]
    items=[]
    sList=[]
    bList=[]
    for i in range(len(S)):
        if S[i]<=bagSize:
           tmp=bestItemChoice([B[idx] for idx in range(len(B)) if not idx == i],[S[idx] for idx in range(len(S)) if not idx == i], bagSize - S[i])
           allItems.append(B[i]+tmp[0])
           items.append(tmp[1])
           bList.append(B[i])
           sList.append(S[i])
    if len(allItems)==0:
        return [0,None]
    else:
        return [max(allItems),(items[allItems.index(max(allItems))] if type(items[allItems.index(max(allItems))])==list else [items[allItems.index(max(allItems))]])+[bList[allItems.index(max(allItems))]]]

print(bestItemChoice([1,3,5,2],[10,30,5,1],16))