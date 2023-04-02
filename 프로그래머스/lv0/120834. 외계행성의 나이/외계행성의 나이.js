function solution(age) {
    const answer = []
    const alphats = [...'abcdefghijklmnopqrstuvwxyz'];
    const strAge = [...String(age)];
    strAge.forEach(n => answer.push(alphats[n]));
    return answer.join("")
}