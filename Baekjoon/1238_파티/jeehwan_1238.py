'''

다시 돌아온,

다익스트라 알고리즘

갈떄 다익스트라 한번
올떄, x 기준 다익스트라 한번

그치만 2번의 다익스트라를 한다.!
함수 사용할때마다 distance배열을 사용해서 쓰자!
2개의 distance를 사용하는것이 아니라! 

저번 풀이에서 배우자
'''



import heapq
import sys

def dijkstra(start):
    q = []
    #이 풀이의 point!
    distance = [INF] * (N + 1)
    heapq.heappush(q, (0, start))
    distance[start] = 0

    while q:
        dist, now = heapq.heappop(q)

        if distance[now] < dist:
            continue

        #i는 [좌표, 거리] 이렇게 이루어져 있음
        for i in MAP[now]:

            cost = dist + i[1]

            if cost < distance[i[0]]:
                distance[i[0]] = cost
                heapq.heappush(q, (cost, i[0]))
    return distance



input = sys.stdin.readline
INF = int(1e9)

N, M, X = map(int, input().split())
MAP = [[] for _ in range(N + 1)]

# 초기 MAP 세팅 => 다익스트라 돌리기 편하게!

#단 반향인거 인지하기

for _ in range(M):
    frm, to, cost = map(int, input().split())
    MAP[frm].append((to, cost))


answer = 0

for i in range(1, N + 1):
    #1번 ~ N + 1에서 출발하는 distance 배열을 만든다.
    start = dijkstra(i)
    #도착지 x에서 출발하는 distance 배열을 만든다.
    end = dijkstra(X)

    #결과적으로 1~ n + 1에서 x까지 가는 값과 x에서 다시 i로 돌아가는 값 중에 가장 큰 값을 구한다.
    answer = max(answer, start[X] + end[i])

print(answer)



