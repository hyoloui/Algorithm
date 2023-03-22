function solution(order) {
    return [...order.toString()].filter((num) => {
        if(num == 0) return false;
        return num % 3 == 0        
    }).length
}