def solution(n, control):
    control_map = {
        'w': 1,
        's': -1,
        'd': 10,
        'a': -10
    }

    for c in control:
        n += control_map[c]
    return n
