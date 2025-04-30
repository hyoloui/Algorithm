def solution(dots):
    first = max(dots)[0] - min(dots)[0]
    second = max(dots)[1] - min(dots)[1]
    return first * second