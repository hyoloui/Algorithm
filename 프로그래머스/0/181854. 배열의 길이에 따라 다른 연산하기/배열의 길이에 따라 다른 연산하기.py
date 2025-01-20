def solution(arr, n):
    answer = []
    arr_leng = len(arr)

    for i in range(arr_leng):
        if arr_leng % 2 != 0 and i % 2 == 0:
            answer.append(arr[i] + n)
        elif arr_leng % 2 == 0 and i % 2 != 0:
            answer.append(arr[i] + n)
        else:
            answer.append(arr[i])
            
    return answer
            
            
        

            
    return answer