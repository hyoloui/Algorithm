function solution(n) {
    const pizza = 6;
    
    let lcm = 1
    while(true){
        if((lcm % pizza == 0) && (lcm % n == 0)){
            break
        }
        lcm++;
    }
    return lcm/pizza;
}