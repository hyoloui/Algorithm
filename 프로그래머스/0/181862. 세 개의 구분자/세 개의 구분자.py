def solution(myStr):
    answer = []
        
    temp = ""
    for char in myStr:
        if char not in ['a', 'b', 'c']:
            temp += char
        else:
            if temp:
                answer.append(temp)
                temp = ""
                
    if temp:
        answer.append(temp)

        
    if not answer:
        answer.append("EMPTY")
    return answer