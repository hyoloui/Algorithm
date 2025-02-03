move_dict = {
    'w': 1,
    's': -1,
    'd': 10,
    'a': -10
}    
    
def solution(numLog):
    answer = ''
    
    for i in range(len(numLog) - 1):
        diff = numLog[i+1] - numLog[i]
        answer += next((key for key, value in move_dict.items() if value == diff), '')
    return answer