function solution(cipher, code) {
    let answer = "";
    const cipherArray = [...cipher];
    for (let i = code; i <= cipherArray.length; i += code) {
        answer += cipherArray[i-1];
    }
    return answer;
}