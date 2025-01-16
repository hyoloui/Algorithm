def solution(arr, delete_list):
    answer = []
    for num in arr:
        if num in delete_list : continue
        else : answer.append(num)
           
    return answer