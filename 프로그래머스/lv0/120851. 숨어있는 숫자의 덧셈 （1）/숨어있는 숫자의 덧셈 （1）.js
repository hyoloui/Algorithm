function solution(my_string) {
    var nums = [...my_string].filter((n) => +n)
    var answer = nums.reduce((acc,val) => +acc + +val);
    return answer;
}