function solution(array) {
    // 키값 저장할 객체 생성
    const answer = {};
    let maxCounter = 0;
    let counterResult = -1;
    
    // for문 돌면서 객체 키값을 저장
    for(let i = 0; i < array.length; i++){
        const num = array[i];
        answer[num] = (answer[num] || 0) + 1;
        if(answer[num] > maxCounter){
            maxCounter = answer[num];
            counterResult = num;
        } else if(answer[num] === maxCounter){
            counterResult = -1;
        }
    }
    return counterResult;
}