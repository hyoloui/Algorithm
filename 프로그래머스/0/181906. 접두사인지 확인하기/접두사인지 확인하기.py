def solution(my_string, is_prefix):
    is_include_first = my_string.split(is_prefix)[0] == ''
    if is_include_first : return 1
    else : return 0