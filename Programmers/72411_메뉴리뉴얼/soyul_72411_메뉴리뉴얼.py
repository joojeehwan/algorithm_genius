from itertools import combinations

def solution(orders, course):

    answer = []

    # 알파벳 순서대로 정렬
    orders = sorted(orders)
    orders = list(map(sorted, orders))      # [['A', 'W', 'X'], ['W', 'X', 'Y'], ['X', 'Y', 'Z']]

    # 먼저 조합을 다 만들어서 넣어줌
    can = [[] for _ in range(max(course) + 1)]
    for order in orders:
        for num in course:
            com = list(combinations(order, num))
            for c in com:
                can[num].append(''.join(c))

    # 조합이 각각 몇 개가 들어있는지 dict 안에 넣어줌
    for i in range(course[0], max(course) + 1):
        dict = {}
        for c in can[i]:
            if c in dict:
                dict[c] += 1
            else:
                dict[c] = 1

    # 2명 이상 주문한 것 중 가장 많은 것으로 선택(여러 개가 나올 수 있으니 리스트로)
        max_course = []
        max_cnt = 1
        for c in dict:
            if dict.get(c) == 1:
                continue
            if dict.get(c) > max_cnt:
                max_course = []
                max_course.append(c)

                max_cnt = dict.get(c)
            elif dict.get(c) == max_cnt:
                max_course.append(c)

        for c in max_course:
            answer.append(c)

    return sorted(answer)
