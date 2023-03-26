function solution(my_string, num1, num2) {
    const answer = [...my_string]
    const firstAlp = answer[num1];
    const secondAlp = answer[num2];
    answer.splice(num1, 1, secondAlp);
    answer.splice(num2, 1, firstAlp);
    return answer.join("");
}