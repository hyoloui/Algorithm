def solution(names):
    answer = []
    for n in enumerate(names):
        idx = n[0]
        name = n[1]
        if (idx % 5 == 0):
            answer.append(name)
    return answer