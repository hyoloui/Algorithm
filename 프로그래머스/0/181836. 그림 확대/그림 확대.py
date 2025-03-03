def solution(picture, k):
    answer = []
    for pixel in picture:
        new_pixel = ''.join([x * k for x in pixel])
        for _ in range(k): answer.append(new_pixel)
    return answer