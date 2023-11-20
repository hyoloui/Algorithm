function solution(arr) {
    const answer = [];
    
    for(let i = 0; i < arr.length; i++) {
        const currentNumber = arr[i];
        
        for(let j = 0; j < currentNumber; j++) {
            answer.push(currentNumber);
        }
    }
    return answer;
}