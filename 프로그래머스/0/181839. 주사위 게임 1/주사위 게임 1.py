def solution(a, b):
    # a % 2 와 b % 2는 각각 a와 b가 홀수일 때 1(True), 짝수일 때 0(False)을 반환합니다.
    if a % 2 and b % 2: 
        return a**2 + b**2
    # a % 2 또는 b % 2 중 하나라도 1(True)이면 참입니다.
    elif a % 2 or b % 2: 
        return 2 * (a + b)
    else:
        return abs(a - b)