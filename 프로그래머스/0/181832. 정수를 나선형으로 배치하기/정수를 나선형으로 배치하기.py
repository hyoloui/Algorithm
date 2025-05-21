def solution(n):
    answer = [[0] * n for _ in range(n)]
    dr = [0, 1, 0, -1]
    dc = [1, 0, -1, 0]

    row, col = 0, 0
    num = 1
    direction = 0
    
    while num <= n * n:
        answer[row][col] = num
        num += 1
        
        next_row, next_col = row + dr[direction], col + dc[direction]
        
        if not (0 <= next_row < n and 0 <= next_col < n) or answer[next_row][next_col] != 0:
            direction = (direction + 1) % 4

        row += dr[direction]
        col += dc[direction]
        print(row, col)
    
    return answer