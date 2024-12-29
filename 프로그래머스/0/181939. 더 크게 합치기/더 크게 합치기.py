def solution(a, b):
    st_a, st_b = str(a), str(b)
    case_1 = int(st_a + st_b)
    case_2 = int(st_b + st_a)
    if case_1 >= case_2 :
        return case_1
    else :
        return case_2