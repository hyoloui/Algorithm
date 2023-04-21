function solution(arr, divisor) {
    arr.sort((a,b) => a - b);
    
    const answer = arr.filter(num => num % divisor === 0);
    return answer.length === 0 ? [-1] : answer;
}