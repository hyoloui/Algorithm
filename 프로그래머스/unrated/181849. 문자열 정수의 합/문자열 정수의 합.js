function solution(num_str) {
    const array = [...num_str]
    return array.reduce((sum, i) =>  sum + Number(i), 0)
}