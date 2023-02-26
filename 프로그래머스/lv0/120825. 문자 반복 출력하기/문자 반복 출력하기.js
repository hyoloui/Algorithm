function solution(my_string, n) {
    // 배열로 나누고 전개연산자 사용하여 쪼갬
    // 하나씩 돌면서 문자를 반복
    // 문자열로 모든 요소 연결
    return [...my_string].map(a => a.repeat(n)).join('');
}