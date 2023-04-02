function solution(emergency) {
    const sorted = [...emergency].sort((a,b) => b - a);
    const answer = emergency.map(n => sorted.indexOf(n)+1);
    return answer;
}