def solution(my_strings, parts):
    answer = ''
    length = range(len(my_strings or parts))
    
    for i in length:
        start, end = parts[i][0], parts[i][1]+1
        slicedStr = my_strings[i][start:end]
        answer += slicedStr
        
    return answer