def solution(binomial):
    answer = 0
    plus, minus, multiply = '+','-','*'
    a, op, b = binomial.split(' ')
    a, b = int(a), int(b)
    
    if op == plus :
        answer = a + b
    elif op == minus :
        answer = a - b
    else :
        answer = a * b

    return answer