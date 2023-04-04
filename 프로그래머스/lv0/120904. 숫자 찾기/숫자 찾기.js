function solution(num, k) {
    const answer = [...String(num)].indexOf(String(k));
    return answer < 0 ? answer : answer + 1;
}