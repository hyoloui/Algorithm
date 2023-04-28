function solution(price, money, count) {
    if(calculate(price, count) < money) return 0;
    return calculate(price,count) - money;
}

function calculate(price, count){
    let sum = 0;
    for (let i = 1; i <= count; i++) {
        sum += price * i;
    }
    return sum
}