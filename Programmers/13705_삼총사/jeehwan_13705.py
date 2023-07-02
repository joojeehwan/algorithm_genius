
'''

입출력 예
number	                   result
[-2, 3, 0, 2, -5]	         2
[-3, -2, -1, 0, 1, 2, 3]	 5
[-1, 1, -1, 1]               0

'''

# 모듈 풀이

from itertools import combinations


def solution(number):

    lsts = list(combinations(number, 3))

    answer = 0

    for val1, val2, val3 in lsts:

        if (val1 + val2 + val3) == 0:
            answer += 1

    return answer


#3중 for문
# 인덱스 관련 정의 예민하게
def solution(number):
    answer = 0
    l = len(number)
    for i in range(l-2):
        for j in range(i+1, l-1):
            for k in range(j+1, l):
                # print(number[i],number[j],number[k])
                if number[i]+number[j]+number[k] == 0:
                    answer += 1
    return answer

# dfs 풀이

# 방식 1

def solution(number):
    tot = 0
    def dfs(i, cnt, sum_num):
        nonlocal tot

        if cnt == 3 and not sum_num:
            tot += 1
            return

        if i == len(number):
            return

        if cnt < 3:
            dfs(i+1, cnt+1, sum_num + number[i])
            dfs(i+1, cnt, sum_num)

    dfs(0,0,0)

    answer = tot


    return answer



# 방식 2

def solution(number):
    answer = 0
    n = len(number)
    used = [0] * n

    def nCr(r, start, n, total):
        nonlocal answer
        # 종료파트
        if r <= 0:
            if not total:
                answer += 1
            return

        # 유도파트
        for i in range(start, n):
            if not used[i]:
                used[i] = 1
                nCr(r-1, i, n, total + number[i])
                used[i] = 0


    nCr(3, 0, n, 0)
    return answer