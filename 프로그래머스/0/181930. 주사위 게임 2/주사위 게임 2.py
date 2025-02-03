def solution(a, b, c):
    answer = a + b + c
    
    if a == b and a == c and b == c :
        answer *= (a*a) + (b*b) + (c*c)
        answer *= (a*a*a) + (b*b*b) + (c*c*c)  
    elif a == b or a == c or b == c :
        answer *= (a*a) + (b*b) + (c*c)

    return answer