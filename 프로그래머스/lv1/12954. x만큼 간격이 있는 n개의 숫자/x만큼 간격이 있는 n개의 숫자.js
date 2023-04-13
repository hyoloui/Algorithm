function solution(x, n) {
    var answer = [x];
    for(let i = 1; i < n; i++) {
        answer.push(answer[answer.length - 1] + x)
    }
    return answer;
}