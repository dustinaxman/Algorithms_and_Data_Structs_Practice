def longestCommonSubSeq(str1,str2):
    if len(str1)>0 and len(str2)>0:
        if str1[-1] == str2[-1]:
            return 1+longestCommonSubSeq(str1[:-1], str2[:-1])
        else:
            return max(longestCommonSubSeq(str1[:-1], str2),longestCommonSubSeq(str1, str2[:-1]))
    else:
        return 0

print(longestCommonSubSeq("abdbeusdertaien","dustienaa"))