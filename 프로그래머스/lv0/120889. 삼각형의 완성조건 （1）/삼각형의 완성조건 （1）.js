function solution(sides){
    var sorting = sides.sort((a,b) => b-a);
    return sorting[0]<(sorting[1]+sorting[2]) ? 1 : 2;
}