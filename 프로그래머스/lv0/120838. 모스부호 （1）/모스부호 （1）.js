function solution(letter) {
    let answer = [];
    const morse = { 
    '.-':'a','-...':'b','-.-.':'c','-..':'d','.':'e','..-.':'f',
    '--.':'g','....':'h','..':'i','.---':'j','-.-':'k','.-..':'l',
    '--':'m','-.':'n','---':'o','.--.':'p','--.-':'q','.-.':'r',
    '...':'s','-':'t','..-':'u','...-':'v','.--':'w','-..-':'x',
    '-.--':'y','--..':'z'
    };
    letter = letter.split(" ")
    letter.map(code => answer += morse[code]);
    return answer;
//     answer= ""
//     codes = letter.split()
//     for i in codes:
//         answer += morse[i]

//     return answer
}