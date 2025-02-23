def solution(myString):
    answer = myString.split('x')
    filtered = list(filter(lambda x:x, answer))
    filtered.sort()
    return filtered