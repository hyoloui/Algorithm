def solution(common):
    if common[2] - common[1] == common[1] - common[0]:
        diff = common[1] - common[0]
        return common[-1] + diff
    else:
        ratio = common[1] // common[0]
        return common[-1] * ratio