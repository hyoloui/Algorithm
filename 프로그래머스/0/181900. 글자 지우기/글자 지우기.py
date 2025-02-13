def solution(my_string, indices):
    my_string = list(my_string)

    for i in sorted(indices, reverse=True):  # indices를 역순으로 정렬하여 뒤에서부터 제거
        del my_string[i]  # 해당 인덱스의 문자 제거

    return "".join(my_string) 