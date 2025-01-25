def solution(num_list):
    multiply = 1
    add = 0
    for num in num_list:
        multiply *= num
        add += num
    if multiply < add**2:
        return 1
    else:
        return 0