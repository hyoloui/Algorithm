function solution(i, j, k) {
    let count = 0;
    for (let n = i; n <= j; n++) {
        count += String(n).split('').filter(digit => digit === String(k)).length;
    }
    return count;
}