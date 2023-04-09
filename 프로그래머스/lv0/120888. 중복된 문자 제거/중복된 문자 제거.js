function solution(my_string) {
    const arr1 = [...my_string]
    const arr2 = [...my_string]
    return arr1.filter((element, index) => arr2.indexOf(element) === index).join("");
}