def solution(spell, dic):
    answer = 2
    sorted_spell = sorted(spell)

    for word in dic:
        if len(word) == len(spell):
            sorted_word = sorted(word)
            if sorted_word == sorted_spell:
                answer = 1
                break

    return answer