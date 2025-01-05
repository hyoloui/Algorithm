def solution(num_list):
    last_num = num_list[len(num_list) - 1]
    last_prev_num = num_list[len(num_list) - 2]
    
    if (last_num > last_prev_num):
        num_list.append(last_num - last_prev_num)
    else :
        num_list.append(last_num * 2)
        
    return num_list