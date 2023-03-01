function solution(array) {
    // sort
    // length / 2
    var answer = 0;
    var sorting = array.sort((a,b) => a-b)
    var center = Math.floor(sorting.length / 2);
    return sorting[center];
}