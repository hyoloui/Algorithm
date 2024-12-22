def solution(num_list):
    oddSum = sum(num_list[::2])
    evenSum = sum(num_list[1::2])
    return oddSum if oddSum > evenSum else evenSum