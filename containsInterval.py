def containsInterval(x,intervalVal):
    j=0
    for i in range(0,len(x)):
        while (j<=(len(x)-1)) and (x[j]-x[i]<intervalVal):
            j+=1
        if x[j]-x[i]==intervalVal:
            return True