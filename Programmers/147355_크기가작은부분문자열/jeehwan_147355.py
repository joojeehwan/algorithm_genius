'''

t에서 p의 길이 만큼 부분문자열을 뽑기.

그 중에서, 초기의 주어진 p의 수보다 작거나 같은 것의 횟수 구하기

'''


def solution(t, p):
    answer = 0

    len_t = len(t)
    len_p = len(p)

    for i in range(0, len_t - len_p + 1):

        temp = t[i:i + len_p]
        if temp <= p:
            answer += 1

    return answer




#dfs 부분 문자열


answer = []

target = 2

