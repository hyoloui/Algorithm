def solution(arr, flag):
    answer = []
    for i, n in enumerate(arr):
        if flag[i]:
            add_arr = [arr[i] for x in range(arr[i] * 2)]
            answer += add_arr
        else:
            del answer[len(answer)-n:]
    return answer