def solution(id_pw, db):
    input_id, input_pw = id_pw
    answer = 'fail'

    for user_id, user_pw in db:
        if input_id == user_id:
            if input_pw == user_pw:
                return 'login' 
            else:
                return 'wrong pw'
        
    return answer