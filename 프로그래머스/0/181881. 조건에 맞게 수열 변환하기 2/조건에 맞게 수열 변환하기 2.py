def solution(arr):
    answer = 0
    copy = arr
    history = [arr[:]]

    while arr:
        new_copy = factory(copy)
        if new_copy == copy:
            break
        if new_copy in history:
            break
        else:
            answer += 1
            copy = new_copy[:]
            history.append(copy[:])

    return answer

def factory(arr):
    copy = []
    for i in arr:
        if i >= 50 and i % 2 == 0:
            copy.append(int(i / 2))
        elif i < 50 and i % 2 == 1:
            copy.append(int(i * 2) + 1)
        else:
            copy.append(i)
    return copy