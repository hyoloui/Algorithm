def solution(n_str):
    answer = n_str
    for i,str in enumerate(n_str):
        if (str == '0'):
            answer = n_str[i+1:]
        else: break
    return answer