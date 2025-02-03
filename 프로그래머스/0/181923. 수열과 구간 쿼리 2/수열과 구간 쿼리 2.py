def solution(arr, queries):
    answer = []
    for s, e, k in queries:
        min_val = float('inf')  # 초기화
        for i in range(s, e + 1):
            if arr[i] > k and arr[i] < min_val:
                min_val = arr[i]
        if min_val == float('inf'):  # k보다 큰 값이 없는 경우
            answer.append(-1)
        else:
            answer.append(min_val)
    return answer