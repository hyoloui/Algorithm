function solution(n) {
var answer = 0;

// n까지 하나씩 돌면서 ex(1,2,3..., n)
for(let i = 2; i <= n; i++) {
    // n 이랑 나누어 떨어지는 수는 하나씩 추가
    if(n % i === 0) answer++;
}
    // 1 * n 은 무조건 이니 하나추가
return answer + 1;
}