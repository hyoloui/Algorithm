function solution(s){
    let countingP = 0;
    let countingY = 0;
    
    for (let i = 0; i < s.length; i++) {
        if(s[i] === "p" || s[i] === "P") countingP++;
        if(s[i] === "y" || s[i] === "Y") countingY++;
    }

    return countingP === countingY ? true : false;
}