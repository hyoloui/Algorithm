const readline = require('readline');
const rl = readline.createInterface({
    input: process.stdin,
    output: process.stdout
});

let input = [];

rl.on('line', function (line) {
    input = line.split(' ');
}).on('close', function () {
    // n으로 받은 값 저장
    const n = Number(input[0]);
    // for문으로 n까지 반복
    for(let i = 1; i <= n; i++){
        // 내부에서 repeat 메서드 활용하여 "*" i만큼 반복
        console.log("*".repeat(i))
    }
});