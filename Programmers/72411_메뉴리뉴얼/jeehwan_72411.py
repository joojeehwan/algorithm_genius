from itertools import combinations
from collections import Counter


def solution(orders, course):
    answer = []

    for cos in course:
        # 각각의 코스 요리 갯수
        temp = []
        for order in orders:
            # 조합의 갯수를 구해야한 각각의 오더
            combi = combinations(sorted(order), cos)
            temp += combi
        counter = Counter(temp)
        # key-value같이 들어가있네,, 각각의 cos갯수마다 중복되는 것의 갯수를 센다
        # print(counter)
        # print(max(counter.values()))
        # if len(counter) != 0 and max(counter.values()) != 1:
        #     answer += [''.join(f) for f in counter if counter[f] == max(counter.values())]
        if counter:
            # 제일 많이 나온 조합이 두번 이상 시켜졌다면
            if max(counter.values()) >= 2:
                for key, value in counter.items():
                    # 현재 조합이 가장 많이 시켜졌다면 결과배열에 추가
                    if value == max(counter.values()):
                        answer.append("".join(key))
        # print(max(counter.values()) != 1)
        # if len(counter) != 0 and max(counter.values())
        # 조건 설정하기!

    return sorted(answer)
#다른 식으로도 풀어보기!