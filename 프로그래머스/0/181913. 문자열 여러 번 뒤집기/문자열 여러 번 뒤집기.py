def solution(my_string, queries):
    my_string = list(my_string)  # 문자열을 리스트로 변환
    for q in queries:
        s, e = q[0], q[1]
        my_string[s:e+1] = my_string[s:e+1][::-1]  # 슬라이싱 후 뒤집기
    return "".join(my_string)  # 리스트를 문자열로 변환