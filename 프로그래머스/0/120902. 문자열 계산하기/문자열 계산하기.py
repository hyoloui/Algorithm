def solution(my_string):
    parts = my_string.split()
    answer = int(parts[0])

    for i in range(1, len(parts) ,2):
        sign = parts[i]
        num = int(parts[i + 1])
        if sign == '+':
            answer += num
        else:
            answer -= num

    return answer