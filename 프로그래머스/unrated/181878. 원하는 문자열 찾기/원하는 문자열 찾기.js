function solution(myString, pat) {
    if(myString.length < pat.length) return 0;
    
    const lowStr = myString.toLowerCase();
    const lowPat = pat.toLowerCase();
    
    if(lowStr.indexOf(lowPat) !== -1 ) return 1
    else return 0
}