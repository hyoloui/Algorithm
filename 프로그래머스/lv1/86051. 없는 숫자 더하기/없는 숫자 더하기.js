function solution(numbers) {
    // 0 ~ 9 까지의 수
    const zeroToNine = Array.from(Array(10).keys());
    // 위에 만든 배열에 포함되지 않은 수를 판별하여 배열로 만들기
    const filtered = zeroToNine.filter(num => !numbers.includes(num));
    // reduce메서드로 누산
    return filtered.reduce((acc, curr) => acc + curr);
}