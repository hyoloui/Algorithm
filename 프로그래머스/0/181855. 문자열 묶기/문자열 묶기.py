def solution(strArr):
    length_groups = {}
    for s in strArr:
        length = len(s)
        if length not in length_groups:
            length_groups[length] = []
        length_groups[length].append(s)
        
    max_group_size = max(len(group) for group in length_groups.values())
    return max_group_size
