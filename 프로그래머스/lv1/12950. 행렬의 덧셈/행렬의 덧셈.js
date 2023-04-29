function solution(arr1, arr2) {
    const row = arr1.length;
    const col = arr1[0].length;
    var answer = [];
    
    for(let i = 0; i < row; i++){
        answer.push([]);
        for(let j = 0; j < col; j++){
            answer[i][j] = arr1[i][j] + arr2[i][j];
        }
    }
    return answer;
}