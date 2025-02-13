def solution(my_string):
    answer = []
    ac_A, ac_Z, ac_a, ac_z = ord('A'), ord('Z'), ord('a'), ord('z')
    
    for i in range(ac_A, ac_Z +1):
        answer.append(0)
    for i in range(ac_a, ac_z +1):
        answer.append(0)
    
    for str in my_string:
        ord_str = ord(str)
        if (ord_str > 90): ord_str -= 6
        ord_str -= ac_A
        answer[ord_str] += 1
    
    return answer