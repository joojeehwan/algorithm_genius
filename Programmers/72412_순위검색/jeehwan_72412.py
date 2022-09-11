


'''

https://www.youtube.com/watch?v=izxzh0rQxSI

<해결방향>

신경쓰지 않는 항목(-)에 대해서 미리 만들어 놓음.

하나의 입력이 들어오면, 조건이 만들 수 있는 모든 조합에 대해서 해당하는 위치에 점수(list 형태)를 다 넣을 것이다.

전체 테이블을 1차원 배열이라 생각하자. 전체 테이블의 개수는 (4 * 3 * 3 * 3 = 108개)


ex)

언어(0 ~ 3)     직군(0 ~ 2)       경력(0 ~ 2)      소울푸드(0 ~ 2)     점수
java           backend          junior          pizza            150

2 * 3*3*3   +  1 * 3*3      +   1 * 3       +      2   = 68 번째 인덱스


case는 총 16가지가 나올것(하나의 조건에 대해서, 있고/없고 라서..) => 이를  bit로 풀 수 있을 것. 
하나하나를 원소로 생각하고 집합으로 표현하면, 모든 부분집합(모든 경우의 수)에 대해서 150점을 넣어준다고 생각! 


어떤 쿼리가 들어오더라도, 하나의 인덱스에서만 점수가 이상인지 이진탐색하면 된다.


'''

# 1

# bit + 이진탐색 풀이


from bisect import bisect_left

def solution(info, query):
    # 아래의 dict를 활용해서, 입력으로 받은 문자열을 인덱스로 사용할 것
    word_map = {'-': 0, 'cpp': 1, 'java': 2, 'python': 3,
                'backend': 1, 'frontend': 2,
                'junior': 1, 'senior': 2,
                'chicken': 1, 'pizza': 2}

    # 점수 저장
    score_lst = [[] for _ in range(4 * 3 * 3 * 3)]

    # 입력받은 info문자열 처리
    for string in info:
        # temp = [언어, 직군, 경력, 소울푸드, 점수]
        temp = string.split()
        lst = (word_map[temp[0]] * 3 * 3 * 3,
               word_map[temp[1]] * 3 * 3,
               word_map[temp[2]] * 3,
               word_map[temp[3]])
        score = int(temp[4])

        # bit형태로 부분집합 나타내기 => 조건이 만족하는 모든 부분집합에 점수 넣어주는 작업
        for i in range(1 << 4):
            # 0 - 15까지 진행
            idx = 0
            # 각각의 부분집합(경우의 수)에 대해서 조건 4가지중 포함되어있을 때만, idx로 만든 인덱스 각각 더하면 된다.
            for j in range(4):
                # (1 << j) 만큼 쉬프트 연산한것과 i(경우의 수)를 & 연산을 하면, 해당 경우의 수에 j번째에 값이 있고 없고를 판단 할 수 있음.
                if i & (1 << j):
                    idx += lst[j]

            score_lst[idx].append(score)
    # 쿼리를 처리하기위해서 score에 따라서 score_lst를 오름차순 정렬(0번 인덱스에 가장 작은 값, 점차 커진다)
    for i in range(4 * 3 * 3 * 3):
        score_lst[i] = sorted(score_lst[i])

    answer = []

    for string in query:
        temp = string.split()
        # 쿼리에 해당하는 인덱스를 계산해야 함.
        idx = word_map[temp[0]] * 3 * 3 * 3 + word_map[temp[2]] * 3 * 3 + word_map[temp[4]] * 3 + word_map[temp[6]]
        score = int(temp[7])

        # bisect 모듈 사용하기 => [100 200 300] , 50이 입력이면 0으로 나옴. 100이면 왼쪽(left) 0. 150은 1
        # 이것을 사용해서, "해당점수 이상"이 몇명이나 있는지 구할 수 있음.
        # => 전체 점수의 길이에서, 찾고자 하는 점수의 인덱스번호를 빼주기

        answer.append(len(score_lst[idx]) - bisect_left(score_lst[idx], score))

    return answer


# 2

from itertools import combinations
from bisect import bisect_left


# java backend junior pizza 를 "backendjuniorpizza", "junior pizza" ... ""
# 위와 같이 가능한 모든 경우의 수 dict 에 넣기
def make_case(x, infoDict):
    tempArr = x.split(" ")
    score = int(tempArr[-1])
    for idx in range(5):
        for c in combinations(tempArr[:-1], idx):
            key = "".join(c)
            if key in infoDict:
                infoDict[key].append(score)
            else:
                infoDict[key] = [score]


# 이진탐색으로 queryScore 보다 큰 점수들의 개수 반환
def find_answer(key, queryScore, infoDict):
    if key in infoDict:
        return len(infoDict[key]) - bisect_left(infoDict[key], queryScore)
    return 0


def solution(info, query):
    infoDict = dict()

    for x in info:
        make_case(x, infoDict)

    for key in infoDict.keys():
        infoDict[key].sort()

    answer = []
    for x in query:
        tempArr = list(y for y in x.replace("and", " ").replace("-", "").split(" ") if len(y) > 0)
        queryScore = int(tempArr[-1])
        if len(tempArr) == 1:
            answer.append(find_answer("", queryScore, infoDict))
        else:
            answer.append(find_answer("".join(tempArr[:-1]), queryScore, infoDict))

    return answer



#우수한 풀이

def solution(info, query):
    data = dict()
    for a in ['cpp', 'java', 'python', '-']:
        for b in ['backend', 'frontend', '-']:
            for c in ['junior', 'senior', '-']:
                for d in ['chicken', 'pizza', '-']:
                    data.setdefault((a, b, c, d), list())
    for i in info:
        i = i.split()
        for a in [i[0], '-']:
            for b in [i[1], '-']:
                for c in [i[2], '-']:
                    for d in [i[3], '-']:
                        data[(a, b, c, d)].append(int(i[4]))

    for k in data:
        data[k].sort()

        # print(k, data[k])

    answer = list()
    for q in query:
        q = q.split()

        pool = data[(q[0], q[2], q[4], q[6])]
        find = int(q[7])
        l = 0
        r = len(pool)
        mid = 0
        while l < r:
            mid = (r+l)//2
            if pool[mid] >= find:
                r = mid
            else:
                l = mid+1
            # print(l, r, mid, answer)
        # answer.append((pool, find, mid))
        answer.append(len(pool)-l)

    return answer








