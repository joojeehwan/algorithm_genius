'''

2차원 다익스트라 문제

보통의 최단거리의 문제에선 비용으로 1차원 다익스트라를 진행.

'''

import heapq
from math import inf


# test2 = [1,2,3]
# test = [[1,3,2,4,5],[1,2,3,4,5]]
# test2.sort(reverse=True)

# # sort 작은거 부터 큰거 순서대로 정렬
# print(test2)

def soltuin(alp, cop, problems):
    # 공부 하는 것을 시간 1을 소모해서, 알고력1 증가 // 코딩력1 증가 해주는 문제라고 생각.
    problems += [[0, 0, 1, 0, 1], [0, 0, 0, 1, 1]]

    problems.sort()

    goal_alp = problems[-1][0]  # sort로
    goal_cop = 0

    for alp_req, cop_req, alp_rwd, cop_rwd, cost in problems:
        goal_cop = max(goal_cop, cop_req)

    # 알고력과 코딩력을 각 행과 열로 하는 2차원 다익스트라

    alp = min(alp, goal_alp)
    cop = min(cop, goal_cop)

    # 다익스트라 진행
    distance = [[inf] * (goal_cop + 1) for _ in range(goal_alp + 1)]  # 거리
    q = []
    heapq.heapqpush(q, [0, alp, cop])
    distance[alp][cop] = 0

    while q:
        dis, alp, cop = heapq.heappop(q)

        if distance[alp][cop] < dis:
            continue

        for alp_req, cop_req, alp_rwd, cop_rwd, cost in problems:

            if alp < alp_req or cop < cop_req:
                # 현재 두 능력이 필요한 두 능력보다 전부 부족하면 break
                if alp < alp_req and cop < cop_req:
                    break
                continue

            # 이 문제를 풀게 될 떄 다음 알고력과 코딩력

        nxt_alp = min(alp + alp_rwd, goal_alp)
        nxt_cop = min(cop + cop_rwd, goal_cop)

        if distance[nxt_alp][nxt_cop] > distance[alp][cop] + cost:
            distance[nxt_alp][nxt_cop] = distance[alp][cop] + cost
            heapq.heapqpush(q, [distance[nxt_alp][nxt_cop], nxt_alp, nxt_cop])

    return distance[goal_alp][goal_cop]