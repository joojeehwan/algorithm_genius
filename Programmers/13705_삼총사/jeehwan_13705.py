
'''

입출력 예
number	                   result
[-2, 3, 0, 2, -5]	         2
[-3, -2, -1, 0, 1, 2, 3]	 5
[-1, 1, -1, 1]               0

'''

# 모듈 풀이

#조합 ver1

lst = [1,2,3,4,5]

target = 2

n = len(lst)

answer = []

def dfs1(now_node, candi) :

    if len(candi) == target:
        answer.append(candi[:])
        return

    debug = 1
    for next_node in range(now_node, n):

        candi.append(lst[next_node])
        dfs1(next_node + 1, candi)
        candi.pop()

#dfs1(0, [])
#print(answer)

def dfs2(now_node, candi) :

    if len(candi) == target:
        answer.append(candi[:])
        return

    debug = 1
    for next_node in range(now_node, n) :
        dfs2(next_node + 1, candi + [lst[next_node]])

#dfs2(0, [])
#print(answer)



def dfs3(lev, cnt, candi) :

    #전체를 다 돌고,
    # 이 코드가 있는 이유?!
    # 해당 코드가 없으면, 인덱스의 끝을 넘는 곳까지 가게 됨. 계속 lev + 1을 증가 시키게 되는데,
    # 전체 범위 인덱스를 초과하면 return 해주거나, 막는 부분이 필요함.
    if lev == n :

        if cnt == target:
        #해당 경우의 수의 요소의 갯수가,내가 찾고자 하는 경우의 수 갯수와 똑같다면,
            answer.append(candi[:])
        return

    debug = 1
    candi.append(lst[lev])
    dfs3(lev + 1, cnt + 1, candi)
    candi.pop()
    dfs3(lev + 1, cnt, candi)

dfs3(0, 0, [])
print(answer)

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
        debug = 1
        # 유도파트
        for i in range(start, n):
            total = total + number[i]
            nCr(r-1, i, n, total)
            total = total - number[i]


    nCr(3, 0, n, 0)
    return answer

solution([-2, 3, 0, 2, -5])


from itertools import combinations


def solution1(number):

    lsts = list(combinations(number, 3))

    answer = 0

    for val1, val2, val3 in lsts:

        if (val1 + val2 + val3) == 0:
            answer += 1

    return answer


#3중 for문
# 인덱스 관련 정의 예민하게
def solution2(number):
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

def solution3(number):
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

def solution4(number):
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


# 조합에서 굳이 used를 사용할 필요는 없다.
# used배열 사용하지 않고 한 version

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
            total = total + number[i]
            nCr(r-1, i + 1, n, total)
            total = total - number[i]


    nCr(3, 0, n, 0)
    return answer