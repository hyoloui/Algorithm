def solution(myString, pat):
    reverse = ''
    
    for str in myString:
        if (str == 'A') : reverse += 'B'
        else : reverse += 'A'
        
    if pat in reverse : return 1
    else : return 0