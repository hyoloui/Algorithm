function solution(my_string) {
    const deleteNaN = [...my_string].filter(char => !isNaN(char));
    const sorting = deleteNaN.map(Number).sort((a,b) => a - b);
    return sorting;
}