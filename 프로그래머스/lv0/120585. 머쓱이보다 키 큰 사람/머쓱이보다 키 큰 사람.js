function solution(array, height) {
    var answer = 0;
    array.map(student => {student>height ? answer++ : null})
    return answer;
}