def solution(myString):
    answer = myString.split("x")
    return [len(x) for x in answer]