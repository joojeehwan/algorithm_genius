'''
다익스트라 개념 이해하고 와서 풀어버리자!

어떻게 풀지?!

최단거리가 k보다 먼곳은 배달을 못해, 1번 마을 기준으로!
다익스트라 다 돌리고 나서 distance에 값 for문으로 검사하고
그 값이 k보다 작으면 cnt 늘려서 answer 만들자!
손이 기억하게 만들자 다익스트라!
heapq 쓰는것도 익숙해져야 해!

'''

import heapq


def dijkstra(start, dis, MAP):
    q = []
    heapq.heappush(q, (0, start))
    dis[start] = 0

    while q:
        dist, now = heapq.heappop(q)

        if dis[now] < dist:
            continue

        for i in MAP[now]:
            cost = dist + i[1]

            if cost < dis[i[0]]:
                dis[i[0]] = cost
                heapq.heappush(q, (cost, i[0]))

def solution(N, road, k):
    answer = 0
    
    #1번 노드는 없다!
    MAP = [[] for _ in range(N + 1)]
    INF = int(1e9)
    distance = [INF] * (N + 1)

    #노도 연결정보
    #양방향 연결! frm에서 to로 가는 cost
    for ro in road:
        MAP[ro[0]].append([ro[1], ro[2]])
        MAP[ro[1]].append([ro[0], ro[2]])

    dijkstra(1, distance, MAP)

    for i in range(1, N+1):
        if distance[i] <= k:
            answer += 1
    return answer