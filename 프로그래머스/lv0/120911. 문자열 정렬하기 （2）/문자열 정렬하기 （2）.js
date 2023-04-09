function solution(my_string) {
    let LowerCase = my_string.toLowerCase();
    var answer = [...LowerCase].sort().join("")
    return answer;
}