function solution(dot) {
    const first = dot[0];
    const second = dot[1]
    
    if(first > 0 && second > 0) return 1;
    if(first < 0 && second > 0) return 2;
    if(first < 0 && second < 0) return 3;
    if(first > 0 && second < 0) return 4;
}