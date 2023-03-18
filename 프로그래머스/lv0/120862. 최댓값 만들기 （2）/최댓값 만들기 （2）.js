function solution(numbers) {
    // 내림차순 정렬을 해놓은 변수를 하나 만든다.
    const descendingNumbers = numbers.sort((a,b) => b - a);
    const desMaxValue = descendingNumbers[0] * descendingNumbers[1];
    // 오름차순 정렬을 해놓은 변수도 만든다.
    const ascendingNumbers = numbers.sort((a,b) => a - b);
    const asMaxValue = ascendingNumbers[0] * ascendingNumbers[1];
    
    // 둘을 비교하여 큰 값을 리턴한다.
    return desMaxValue > asMaxValue ? desMaxValue : asMaxValue;
}