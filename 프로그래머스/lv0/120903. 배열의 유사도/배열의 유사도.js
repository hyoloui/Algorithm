function solution(s1, s2) {
    // 배열 map 돌기
    // 안에서 find g하기
    var answer = 0;
    s1.map(str1 => s2.find(str2 => (str1 === str2)&& ++answer))
    return answer;
}