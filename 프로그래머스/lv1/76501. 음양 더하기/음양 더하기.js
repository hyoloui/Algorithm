function solution(absolutes, signs) {
    let sum = 0;
    
    signs.forEach((sign, index) => {
        sign ?
            sum += absolutes[index]:
            sum -= absolutes[index];
    })
    return sum
}