function solution(arr) {
    if(arr.length === 1 || arr.length === 0) return [-1];
    
    let min = arr[0];
    for(let i = 1; i <= arr.length; i++){
        if(min > arr[i]) min = arr[i];
    }
    
    let idx = arr.indexOf(min);
    arr.splice(idx, 1);
    return arr;
}