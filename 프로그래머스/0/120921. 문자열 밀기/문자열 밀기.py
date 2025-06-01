def solution(A, B):
    answer = 0
    copy = A
    
    for i in range(len(A)):
        if copy == B: break
        copy = copy[-1] + copy[:-1]
        answer += 1

    if len(A) == answer :
        return -1
    
    return answer