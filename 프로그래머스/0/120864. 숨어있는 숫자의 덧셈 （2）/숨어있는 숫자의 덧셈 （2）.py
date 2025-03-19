def solution(my_string):
    answer = 0
    num_str = ''
    for char in my_string:
        if char.isdigit():
            num_str += char
        else:
            if num_str:
                answer += int(num_str)
                num_str = ''
    if num_str:
        answer += int(num_str)
    return answer