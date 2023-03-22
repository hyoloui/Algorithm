function solution(order) {
    // 필터로 length 조지기
    const stringy = [...order.toString()]
    const filtering = stringy.filter((num) => num == 3 || num == 6 || num == 9)
    return filtering.length
}