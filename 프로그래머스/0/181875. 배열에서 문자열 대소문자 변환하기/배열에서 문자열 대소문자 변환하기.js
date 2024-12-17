const solution = (strArr) => strArr.map((str, idx) => convertStr(str, idx))
const isEven = (i) => i % 2 === 0;
const convertStr = (str, idx) => isEven(idx) ? str.toLowerCase() : str.toUpperCase();