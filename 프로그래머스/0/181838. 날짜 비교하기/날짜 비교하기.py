def solution(date1, date2):
    is_date1_before_date2 = date1 < date2
    if is_date1_before_date2:
        return 1
    else:
        return 0