def solution(s):
    answer = 0
    arr = s.split(' ')
    for i,n in enumerate(arr):
        if n == 'Z':
            answer -= int(arr[i-1])
        else:
            answer += int(n)
    return answer