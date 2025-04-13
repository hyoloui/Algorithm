def solution(quiz):
    answer = []
    
    for problem in quiz:
        first, sign, second, equal, last = problem.split()
        ox = ''
        
        if sign == '+':
            if int(first) + int(second) == int(last):
                ox = 'O'
            else:
                ox = 'X'
                
        if sign == '-':
            if int(first) - int(second) == int(last):
                ox = 'O'
            else:
                ox = 'X'
                
        answer += ox
            
    return answer