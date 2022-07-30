''''


아 이건 뭐야,,

어디까지 같이 가니? 그게 중요한데,,

요금 = dijkstra(출발점, k) +  dijkstra(k, A) +  dijkstra(K, B)

모든 노드를 반복문 돌면서  K에 대입하고, 그 결과 값이 요금을 비교하면서
가장 작은 요금을 찾아보자!

아까랑 기본적인 세팅은 똑같애!


아 이거 distance 배열 다익스트라 돌때마다 갱신해줘야 해 ㅠㅠ
배달 풀듯이 그냥 distance 밖에다 두고 해서 하하,,,

'''

import heapq


def dijkstra(start, goal, num, MAP):
    q = []
    INF = int(1e9)
    heapq.heappush(q, (0, start))
    # 아 디스턴스 배열 항상 여기 있어야 한다...! 각각의 다익스트라마다 초기화 해야 하니깐!
    distance = [INF] * (num + 1)
    distance[start] = 0

    while q:
        dist, now = heapq.heappop(q)

        if distance[now] < dist:
            continue

        for i in MAP[now]:
            cost = dist + i[1]

            if cost < distance[i[0]]:
                distance[i[0]] = cost
                heapq.heappush(q, (cost, i[0]))

    return distance[goal]


def solution(n, s, a, b, fares):
    MAP = [[] for _ in range(n + 1)]

    # 노드 다시 재정리!
    for fare in fares:
        MAP[fare[0]].append([fare[1], fare[2]])
        MAP[fare[1]].append([fare[0], fare[2]])

    # 시작지점에서부터 따로 집으로 합승 안함
    answer = dijkstra(s, a, n, MAP) + dijkstra(s, b, n, MAP)

    # 합승
    for i in range(1, n + 1):
        # s == i가 되는 순간 스타트 부터 따로 집으로 가는거자나?!
        if s != i:
            answer = min(answer, dijkstra(s, i, n, MAP) + dijkstra(i, a, n, MAP) + dijkstra(i, b, n, MAP))

    return answer