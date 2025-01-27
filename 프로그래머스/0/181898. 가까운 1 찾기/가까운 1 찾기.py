def solution(arr, idx):
    slicedFront = arr[:idx]
    slicedBack = arr[idx:]
    
    if 1 not in slicedBack : return -1

    frontLength = len(slicedFront)
    backIdx = slicedBack.index(1)
    
    return frontLength + backIdx