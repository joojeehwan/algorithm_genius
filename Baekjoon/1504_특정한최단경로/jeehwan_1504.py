'''

기본 다익스트라 문제

다익스트라 이제 안보고도 쓸 수 잇어야 돼

매번 암기하려 노력하자... 손이 기억하도록, dfs/bfs 처럼

내 velog 참고

https://velog.io/@meanstrike/%EC%9D%B4%EC%BD%94%ED%85%8C-%EC%B5%9C%EB%8B%A8-%EA%B2%BD%EB%A1%9C
'''



import heapq
import sys
input = sys.stdin.readline
INF = int(1e9)

N, E = map(int, input().split())

MAP = [[] for _ in range(N + 1)]

distance = [INF] * (N + 1)

for _ in range(E):

    #양방향 그래프
    frm, to, value = map(int, input().split())
    MAP[frm].append((to, value))
    MAP[to].append((frm, value))


def dijkstra(start):

    q = []
    heapq.heappush(q, (0, start))
    distance[start] = 0

    while q:

        dist, now = heapq.heappop()

        if distance[now] < dist:
            continue

        for next_node, value in MAP[now] :

            cost = dist + value

            #현재 노드를 거쳐서, 다른 노드로 이동하는 거리가 더 짧은 경우
            if cost < distance[next_node] :
                distance[next_node] = cost
                heapq.heappush(q, (cost, next_node))


    return distance

'''
v1과 v2를 반드시 거쳐야 하므로 다음과 같은 경우를 고려해주면 된다.

1 => v1 => v2 => N

1 => v2 => v1 => N

'''
v1, v2 = map(int, input().split())

# 출발점이 각각 1, v1, v2일 때의 최단 거리 배열
original_distance = dijkstra(1)
v1_distance = dijkstra(v1)
v2_distance = dijkstra(v2)

v1_path = original_distance[v1] + v1_distance[v2] + v2_distance[v]
v2_path = original_distance[v2] + v2_distance[v1] + v1_distance[v]

result = min(v1_path, v2_path)
print(result if result < INF else -1)
