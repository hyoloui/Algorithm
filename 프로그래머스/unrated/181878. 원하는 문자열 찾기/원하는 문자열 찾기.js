function solution(myString, pat) {
    if(myString.length < pat.length) return 0;
    
    const lowStr = myString.toLowerCase();
    const lowPat = pat.toLowerCase();
    
    return lowStr.includes(lowPat) ? 1 : 0
}