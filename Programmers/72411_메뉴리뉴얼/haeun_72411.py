"""
course에 있는 숫자 순서대로 찾아보는데
백트랙킹 할 부분이 그 숫자만큼 주문한 사람이 2명 이상인가밖에 거를 점이 없는 것 같은데
어찌된거죠
내 점수 : 1101(+7)
"""
from itertools import combinations

def solution(orders, course):
    answer = []

    # 손님의 수
    order_count = len(orders)
    # 각 손님마다 주문한 메뉴의 개수 저장
    order_length = [0] * order_count
    for i in range(order_count):
        order_length[i] = len(orders[i])

    # 오름차순 정렬
    order_length.sort()

    # 최대값과 그 보다 하나 앞의 값을 비교해서 작다면 하나 앞의 값을,
    # 같다면 최대 값으로 2번 이상 최대 주문한 메뉴의 개수 찾기.
    if order_length[order_count-1] > order_length[order_count-2]:
        max_order_length = order_length[order_count-2]
    else:
        max_order_length = order_length[order_count-1]

    # 목표하는 코스의 개수마다 찾아본다. 2개, 3개 등등..
    for goal_count in course:
        # 메뉴의 조합을 저장할 딕셔너리
        order_combs = dict()
        if goal_count > max_order_length:
            # 원하는 개수만큼 2명의 손님이 메뉴를 주문한 적이 없다.
            break
        # 손님이 주문한 메뉴들의 목록을 하나씩 돌면서
        # 원하는 개수에서 가장 많이 주문된 것을 구해야한다.
        goal_max_order_length = 1

        for order in orders:
            # XW랑 WX를 같은 조합으로 만들기 위해 문자열을 리스트로 바꾸고 정렬한다.
            list_order = sorted(list(order))
            list_order_comb = list(combinations(list_order, goal_count))

            # 몇번 주문되었는지 딕셔너리에 저장하면서 최대 주문된 횟수를 찾는다.
            for order_comb in list_order_comb:
                if order_combs.get(order_comb):
                    order_combs[order_comb] += 1
                    if order_combs[order_comb] > goal_max_order_length:
                        goal_max_order_length = order_combs[order_comb]
                else:
                    order_combs[order_comb] = 1

        # 만약 2번 이상 주문된 조합이 없다면 만들 수 없다.
        if goal_max_order_length == 1:
            continue

        # 이번에 만든 조합들 중에서 최대 주문된 횟수를 가진 조합만 정답에 문자열로 바꿔서 넣는다.
        for goal_count_order in order_combs:
            if order_combs[goal_count_order] == goal_max_order_length:
                answer.append("".join(goal_count_order))
    # 정렬해서 반환한다.
    return sorted(answer)



order_string = ["ABCDE", "AB", "CD", "ADE", "XYZ", "XYZ", "ACD"]
course_string = [2,3,5]
print(solution(order_string, course_string))