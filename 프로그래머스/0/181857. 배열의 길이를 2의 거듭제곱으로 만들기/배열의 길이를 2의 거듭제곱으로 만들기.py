def solution(arr):
    a = 1
    while len(arr) > a:
        if len(arr) > a:
            a = a * 2
    zeroLen = a - len(arr)
    return arr + [0] * zeroLen