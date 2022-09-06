'''

참고

https://www.youtube.com/watch?v=izxzh0rQxSI


-(빼기) 항목을 미리 만들어 놓고, 한번에 찾아서 처리

하나의 입력이 들어오면, 조건을 신경쓰지 않는 것 포함해서, 모든 조합에 대해서, 값을 미리 가지고 있다


4 * 3 * 3 * 3 = 108개






'''


# 유투브 풀이



# 이상적으로 잘 푼 풀이

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









