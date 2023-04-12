function solution(arr) {
    const num = arr.reduce((prev, curr) => prev + curr);
    return num/arr.length
}