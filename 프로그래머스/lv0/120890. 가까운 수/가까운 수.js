function solution(array, n) {
    array.sort()
    let answer = 0;
    let min = 100;
    array.forEach(ele => {
        if(min > Math.abs(n-ele)) {
            min = Math.abs(n-ele);
            answer = ele;
        }
    })
    return answer;
}