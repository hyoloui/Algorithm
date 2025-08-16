def solution(s):
    numbers = list(map(int, s.split()))
    
    # 최소값과 최대값 찾기
    min_val = min(numbers)
    max_val = max(numbers)
    
    # 결과를 문자열 형태로 반환
    return f"{min_val} {max_val}"