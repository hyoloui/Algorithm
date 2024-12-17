const solution = (strArr) => strArr.map((str, idx) => isEven(idx) ? str.toLowerCase() : str.toUpperCase());
const isEven = (i) => i % 2 === 0;