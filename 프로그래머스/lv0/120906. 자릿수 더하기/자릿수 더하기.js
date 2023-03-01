function solution(n) {
    var answer = 0;
    var arrStr = [...String(n)].map((n) => answer+=(+n))
    return answer;
}