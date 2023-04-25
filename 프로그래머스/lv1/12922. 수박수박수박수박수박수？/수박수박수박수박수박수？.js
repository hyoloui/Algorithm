function solution(n) {
    const repeated = '수박'.repeat(n);
    return repeated.slice(0, repeated.length / 2);
}