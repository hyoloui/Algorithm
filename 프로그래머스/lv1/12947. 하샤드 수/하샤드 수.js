function solution(x) {
    const shallowCopy = [...x.toString()]
    const sum = shallowCopy.reduce((acc,curr) => (+acc)+(+curr), 0);
    return x % sum === 0 ? true : false
}