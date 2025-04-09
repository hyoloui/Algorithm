def solution(s):
    char_counts = {}
    # 딕셔너리에 각 문자의 등장 횟수를 저장합니다.
    for char in s:
        char_counts[char] = char_counts.get(char, 0) + 1

    once_appeared = []
    for char, count in char_counts.items():
        if count == 1:
            once_appeared.append(char)
            
    return "".join(sorted(once_appeared))