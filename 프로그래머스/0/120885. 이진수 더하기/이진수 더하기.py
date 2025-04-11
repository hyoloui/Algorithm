def solution(bin1, bin2):
    decimal_bin1 = int(bin1, 2)
    decimal_bin2 = int(bin2, 2)
    sum_decimal = decimal_bin1 + decimal_bin2
    answer = bin(sum_decimal)[2:]
    return answer