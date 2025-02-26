def solution(arr, k):
    answer = []
    for n in arr:
        if n not in answer:
            answer.append(n)

    if len(answer) > k:
        return answer[:k]
    else:
        return answer + [-1] * (k - len(answer))