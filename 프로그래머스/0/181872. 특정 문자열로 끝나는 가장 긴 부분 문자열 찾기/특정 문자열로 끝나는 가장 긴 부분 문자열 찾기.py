def solution(myString, pat):
    find_pat_idx = len(myString) - myString[::-1].find(pat[::-1])
    return myString[:find_pat_idx]