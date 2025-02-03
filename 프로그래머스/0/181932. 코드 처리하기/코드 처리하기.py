def solution(code):
    mode = 0
    ret = ''
    
    for i, str in enumerate(code):
        if mode == 0:
            if str == '1':
                mode = 1
                continue
            if i%2 == 0: ret += str 
            
        if mode == 1:    
            if str == '1':
                mode = 0
                continue
            if i%2: ret += str
    
    if ret == '' : return 'EMPTY'
    return ret