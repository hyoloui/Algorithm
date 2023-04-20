function solution(a, b) {
    let result = 0;

    if (b > a) {
        let tmp = b;
        b = a;
        a = tmp;
    }

    for (let i = b; i <= a; i++) {
        result += i;
    }

    return result;
}