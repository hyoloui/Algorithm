function solution(arr) {
    return arr.reduce((acc, cur) => {
        if (cur >= 50){
            if (cur % 2 === 0) acc.push(cur / 2);
            else acc.push(cur)
        } else {
            if  (cur % 2 !== 0) acc.push(cur * 2);
            else acc.push(cur)
        }
        return acc
    }, [])
}