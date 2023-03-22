function solution(score) {
    const sumScore = score.map((s) => s[0] + s[1])
    const sortScore = [...sumScore].sort((a,b) => b-a);

   return sumScore.map((v) => sortScore.indexOf(v) + 1)
}