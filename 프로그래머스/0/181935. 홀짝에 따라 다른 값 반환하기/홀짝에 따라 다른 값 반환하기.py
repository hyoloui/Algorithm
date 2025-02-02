def solution(n):
    answer = 0
    
    for i in range(n+1):
        if isEven(n) :
            if isEven(i): answer += i ** 2
        else :
            if not isEven(i) : answer += i
        
    return answer

def isEven(n): return n % 2 == 0