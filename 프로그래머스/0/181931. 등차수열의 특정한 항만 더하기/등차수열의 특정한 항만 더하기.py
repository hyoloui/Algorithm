def solution(a, d, included):
    answer = 0
    
    for i, bool in enumerate(included):
        curNum = a + (d * i)
        if bool: answer += curNum
        
    return answer