def solution(number, n, m):
    case_1 = number / n
    case_2 = number / m
    if case_1.is_integer() and case_2.is_integer():
        return 1
    else : return 0