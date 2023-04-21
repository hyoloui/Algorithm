function solution(phone_number) {
    let shallowCopy = [...phone_number]
    for (let i = 0; i < shallowCopy.length - 4; i++){
        shallowCopy[i] = '*'
    }
    return shallowCopy.join("");
}

// Test Code
console.log(solution("01099990999"));
console.log(solution("06451240999"));
console.log(solution("0123456789"));
console.log(solution("1234123412341234"));
