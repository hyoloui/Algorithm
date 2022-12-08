function solution(keyinput, board) {
    const answer = [0, 0];
    
    // 맵의 크기
    const map = 
          [ Math.abs( Math.floor(board[0] / 2) ), 
           Math.abs( Math.floor(board[1] / 2) ) ];

    for(key of keyinput){
        // 입력 값 계산
        switch(key){
            case "left" : answer[0] -= 1; break;
            case "right" : answer[0] += 1; break;
            case "down" : answer[1] -= 1; break;
            case "up" : answer[1] += 1; break;
        }
        // answer[0] 의 절댓값이 맵의 크기보다 크다면 map[0]의 크기로 반환
        if(answer[0] < map[0] * -1){
            answer[0] = map[0] * -1;
         } else if (answer[0] > map[0]){
             answer[0] = map[0]
         }
        // answer[1] 의 절댓값이 맵의 크기보다 크다면 map[1]의 크기로 반환
        if(answer[1] < map[1] * -1){
            answer[1] = map[1] * -1;
        } else if (answer[1] > map[1]){
             answer[1] = map[1]
         }
    }
    return answer
}
