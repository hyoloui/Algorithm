function solution(s) {
  // 문자열이 길이가 4 또는 6인지 검사
  if (s.length !== 4 && s.length !== 6) {
    return false;
  }

  // 문자열의 모든 문자가 숫자인지 검사
  for (let i = 0; i < s.length; i++) {
    if (isNaN(s[i])) {
      return false;
    }
  }

  // 모든 조건을 통과하면 true 반환
  return true;
}
