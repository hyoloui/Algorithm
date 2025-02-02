def solution(str1, str2):
    answer = ''
    for i, str in enumerate(str1):
        answer += str
        answer += str2[i]
    return answer