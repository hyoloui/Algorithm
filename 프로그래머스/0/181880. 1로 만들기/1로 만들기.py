def solution(num_list):
    answer = 0
    for n in num_list:
        while n != 1:
            answer += 1
            if n % 2 == 0:
                n = n / 2
            else :
                n = (n - 1) / 2
                
    return answer