def solution(polynomial):
    answer = []
    xNum = 0
    num = 0
    
    arr = polynomial.split(" + ")
    for n in arr:
        if n.endswith('x'):
            if n[0] == 'x': xNum += 1
            else: xNum += int(n[:-1])
        else:
            num += int(n)
            
    if xNum:
        if xNum == 1: answer.append('x')
        else: answer.append(f'{xNum}x')
    if xNum and num: answer.append(' + ')
    if num: answer.append(str(num))
    
    return ''.join(answer)