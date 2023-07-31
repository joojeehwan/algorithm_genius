'''

한번에 푼 문제

split의 기능 잘 사용하기

'''


def solution(s):
    answer = ''

    lst = list(map(int, s.split()))
    MAX = str(max(lst))
    MIN = str(min(lst))

    answer += (MIN + " " + MAX)

    return answer