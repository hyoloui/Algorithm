function solution(my_string) {
    const spreadArray = [...my_string];
    const lowerCase = (str) => str.toLowerCase();
    const upperCase = (str) => str.toUpperCase();
    return spreadArray.map(str => (str === upperCase(str)) ? lowerCase(str) : upperCase(str)).join("");
}
