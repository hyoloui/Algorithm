function solution(s) {
    const middle = Math.floor(s.length / 2);
    
    if(s.length % 2 === 0) { // 짝수
        return s.slice(middle - 1, middle + 1);
    } else { // 홀수
        return s.charAt(middle);
    }
};
