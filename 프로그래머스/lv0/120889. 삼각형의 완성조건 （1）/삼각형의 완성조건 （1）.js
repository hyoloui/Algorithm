function solution(sides) {
    const maxx = Math.max(...sides);
    let filtered = sides.reduce((a,b) => a+b)-Math.max(...sides);

    return filtered > Math.max(...sides) ? 1 : 2;
}
