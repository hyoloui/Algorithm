def solution(myString, pat):
    strRange = range(len(myString))
    answer = 0
    for x in strRange:
        patLen = len(pat)
        sliceStr = myString[x:x+patLen]
        if pat in sliceStr:
            answer += 1
            
    return answer