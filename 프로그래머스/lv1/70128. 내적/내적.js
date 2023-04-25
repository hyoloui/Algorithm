function solution(a, b) {
    let answer = 0;
    let index = 0;
    while (index < a.length) {
        answer += a[index] * b[index];
        index++;
    }
    return answer;
}