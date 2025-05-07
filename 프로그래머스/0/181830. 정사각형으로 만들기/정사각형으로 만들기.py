def solution(arr):
    rows = len(arr)
    cols = len(arr[0]) if rows > 0 else 0
    square_len = max(rows, cols)

    answer = [[0 for _ in range(square_len)] for _ in range(square_len)]

    for i in range(rows):
        for j in range(cols):
            answer[i][j] = arr[i][j]
                
    return answer