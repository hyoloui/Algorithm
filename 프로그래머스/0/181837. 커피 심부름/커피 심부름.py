def solution(order):
    answer = 0
    for menu in order:
        if menu.find('cafelatte') < 0:
            answer += 4500
        else:
            answer += 5000
    return answer