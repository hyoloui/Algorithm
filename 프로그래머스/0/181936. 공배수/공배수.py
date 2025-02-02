def solution(number, n, m):
    c1 = number / n
    c2 = number / m

    if c1.is_integer() and c2.is_integer(): return 1
    else : return 0