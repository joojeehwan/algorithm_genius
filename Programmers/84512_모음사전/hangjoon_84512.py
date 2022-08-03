def ex_search(word, now=''):
    global answer
    # 종료조건
    if len(now) >= 6:
        answer -= 1
        return 0
    if word == now:
        return 1
    # 진행 중
    for letter in ['A', 'E', 'I', 'O', 'U']:
        answer += 1
        if ex_search(word, now + letter):
            return 1


def solution(word):
    global answer
    answer = 0
    ex_search(word)
    return answer


print(solution("AAAAE"))
print(solution("AAAE"))
print(solution("I"))
print(solution("EIO"))
