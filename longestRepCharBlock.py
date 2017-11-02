#given string find start index of longest block of repeated characters
def longestRefCharBlock(tmpString):
    idx = 0
    tmpIdx = 0
    largestCount = 0
    tmpCount=0
    str = list(tmpString)
    for i in range(1, len(str)):
        if str[i] == str[i - 1]:
            tmpCount += 1
        else:
            if tmpCount > largestCount:
                largestCount = tmpCount
                idx = tmpIdx
            tmpCount = 0
            tmpIdx = i
    return idx
print(longestRefCharBlock("jddlskaaapekpppppddd"))