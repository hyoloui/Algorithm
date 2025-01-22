def solution(arr1, arr2):
    leng1, leng2 = len(arr1), len(arr2)
    
    if leng1 > leng2 : return 1
    elif leng1 < leng2 : return  -1

    else :
        sum1, sum2 = sum(arr1), sum(arr2)
        if sum1 > sum2 : return 1
        elif sum1 < sum2 : return -1
        else : return 0