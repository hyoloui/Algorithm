function solution(box, n) {
    const maxWidth = box[0]-(box[0] % n);
    const maxHeight = box[1]-(box[1] % n);
    const maxLength = box[2]-(box[2] % n);
    const maxVolume = maxWidth * maxHeight * maxLength;
    const boxVolume = n ** 3
    return maxVolume / boxVolume;
}