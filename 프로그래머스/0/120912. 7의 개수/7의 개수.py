def solution(array):
    answer = 0
    long_str = "".join(map(str, array))
    for char in long_str:
        if char == '7':
            answer += 1
    return answer