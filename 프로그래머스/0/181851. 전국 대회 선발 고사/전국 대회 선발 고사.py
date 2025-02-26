def solution(rank, attendance):
    answer = 0
    result = [x for x, y in zip(rank, attendance) if y]
    result.sort()
    aIdx, bIdx, cIdx = [rank.index(val) for val in result[:3]]
    
    answer += 10000 * aIdx
    answer += 100 * bIdx
    answer += cIdx
    return answer