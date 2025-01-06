def solution(a, b):
    case_1 = int( str(a) + str(b) )
    case_2 = 2 * a * b
    return case_1 if case_1 >= case_2 else case_2