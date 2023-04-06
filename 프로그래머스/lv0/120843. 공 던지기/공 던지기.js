function solution(numbers, k) {
    let repeatArray = new Array(k).fill(numbers).flat();
    console.log(repeatArray)
    return 3 <= k ? repeatArray[(k * 2) - 2] : repeatArray[k];
}