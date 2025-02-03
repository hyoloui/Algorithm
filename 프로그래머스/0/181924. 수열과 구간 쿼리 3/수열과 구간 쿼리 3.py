def solution(arr, queries):
    for a, b in queries:
        copy_a = arr[a]
        arr[a] = arr[b]
        arr[b] = copy_a

    return arr