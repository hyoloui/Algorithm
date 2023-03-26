function solution(numbers, direction) {
    let num = [];
    
    if(direction === "right"){
        num = numbers.splice(numbers.length - 1, 1);
        num.push.apply(num,numbers);
        return num
    }
        
    if(direction === "left"){
        num = numbers.splice(0, 1);
        numbers.push.apply(numbers, num);
        return numbers
    }
}