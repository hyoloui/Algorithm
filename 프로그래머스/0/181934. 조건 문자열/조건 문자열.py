def solution(ineq, eq, n, m):
    isEq = eq == '='
    isOver = ineq == '<'
    
    if isEq :
        if isOver and n <= m : return 1
        elif not isOver and n >= m : return 1
        else : return 0
        
    elif not isEq:
        if isOver and n < m : return 1
        elif not isOver and n > m : return 1
        else : return 0
    
    