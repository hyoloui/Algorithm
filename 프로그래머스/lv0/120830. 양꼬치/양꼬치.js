function solution(n, k) {
    var meet = 12000 * n;
    var drink = 2000 * k;
    var service = Math.floor(n / 10) * 2000
    return meet + drink - service;
}