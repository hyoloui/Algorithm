def solution(arr):
    find_two_idx = []
    
    for i, num in enumerate(arr):
        if num == 2 : find_two_idx.append(i)
        
    if not find_two_idx : return [-1]

    first, last = find_two_idx[0], find_two_idx[-1]
    return arr[first:last+1]