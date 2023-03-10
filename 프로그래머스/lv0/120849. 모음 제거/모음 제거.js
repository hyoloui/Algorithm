function solution(my_string) {
    // const arr = ["a","e","i","o","u"]
    // const answer = [...my_string].filter(str => arr.map(a => !arr.includes(a)));
    return my_string.replace(/[aeiou]/g, "");
}