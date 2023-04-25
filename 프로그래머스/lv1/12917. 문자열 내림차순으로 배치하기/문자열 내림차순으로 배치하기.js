function solution(s) {
    const copyShallow = [...s];
    const sorted = copyShallow.sort((a,b) => b.charCodeAt(b) - a.charCodeAt(a));
    return sorted.join("");
}