function solution(n) {
    // n 이하의 짝수를 구함
    // 구한 짝수를 더한 값을 answer에 대입
    var answer = 0;
    for (let i = 2; i <= n; i++) {
        i % 2==0 ? answer += i : null
    }
    return answer;
}