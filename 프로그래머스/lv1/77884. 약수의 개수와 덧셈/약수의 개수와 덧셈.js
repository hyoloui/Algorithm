function solution(left, right) {
    let answer = 0;
    for (let i = left; i <= right; i++){
        calculate(i) % 2 === 0 ? answer+=i : answer-=i;
    }
    return answer;
}

function calculate(i){
    let num = 0;
    for (let n = 1; n <= i; n++){
        if(i % n === 0) num++;
    }
    return num;
}