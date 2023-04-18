function solution(n) {
    let answer = []
    let str = [...String(n)];
    for (let i = 0; i < str.length; i++) {
        answer.push(+str[str.length - 1 - i])
    }
    return answer;
}