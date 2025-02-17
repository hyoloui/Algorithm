def solution(str_list):
    answer = []

    l_idx = -1
    r_idx = -1

    if 'l' in str_list:
        l_idx = str_list.index('l')
    if 'r' in str_list:
        r_idx = str_list.index('r')

    if l_idx != -1 and r_idx != -1:  # "l"과 "r" 모두 존재하는 경우
        first_idx = min(l_idx, r_idx)
        if first_idx == l_idx:
            answer = str_list[:l_idx]
        else:
            answer = str_list[r_idx + 1:]
    elif l_idx != -1:  # "l"만 존재하는 경우
        answer = str_list[:l_idx]
    elif r_idx != -1:  # "r"만 존재하는 경우
        answer = str_list[r_idx + 1:]
        
    return answer