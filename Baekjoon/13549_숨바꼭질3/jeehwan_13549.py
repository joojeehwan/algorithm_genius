
'''


- 수빈이는 현재 N에 있고, 동생은 K에 있다.

- 수빈이는 걷거나, 순간이동 가능

    - 걷을 때, 1초 후에, x - 1 Ehsms x + 1
    - 순간이동, 0초 후에, 2**x

수빈이가 동생을 찾을 수 있는 가장 빠른 시간이 몇 초 후인지 구하라


sol) 순간 이동과 걷기의 시간(가중치)가 다르므로, 큐 2개로 나뉘어 구현하며 되는데

python의 deque 자체가 양방향 이므로, 이를 이용

순간이동 appendleft // 걷는 경우 append
'''

# bfs 풀이
from collections import deque



N, K = map(int, input().split())

visited = [0] * int(10e6)

q = deque()
q.append((N))
visited[N] = True

while q:

    now_node = q.popleft()

    if now_node == K:
        print(visited[now_node])

    else:

        for next_node in (2*now_node, now_node - 1, now_node + 1):

            # 이동 후에 반드시 범위 체크 & 한번도 방문하지 않은 곳
            if 0 <= next_node < 100001 and visited[next_node] :
                #순간이동
                if next_node == 2 * now_node:
                    #visited 배열에 값을 활용해 가중치를 표현
                    visited[next_node] = visited[now_node]
                    q.appendleft((next_node))
                # 걸어서
                else:
                    visited[next_node] = visited[now_node] + 1
                    q.append((next_node))




#다익스트르 풀이 

import heapq


def dijkstra(start_node):
    visited = [INF] * 20001
    visited[start_node] = 0
    heapq.heappush(q, (visited[start_node], start_node))  # 해당 노드까지 걸리는 시간(비용) // 노드 번호

    while q:
        cost, now_node = heapq.heappop(q) #최단 거리가 가장 짧은 것, 하나 뽑아서 보자, 지금 여기의 cost는 이전까지의 cost 인것! 드디어 알았다.

        if now_node == k:
            print(cost)
            break


        #기존에 있는 시간 보다 더 걸리면?! 굳이 가지 않아!
        if visited[now_node] < cost:
            continue

        for next_node in (now_node * 2, now_node + 1, now_node - 1):

            # 범위 생각 & 최단거리
            # 순간이동
            if 0 <= next_node < 100001 and cost < visited[next_node] :
                visited[next_node] = cost #가중치 0
                heapq.heappush(q, (visited[next_node], next_node))

            else:
                visited[next_node] = cost + 1
                heapq.heappush(q, (visited[next_node], next_node))



#이렇게 풀수도
# ✨ 입력
import sys
import heapq
input = sys.stdin.readline
N,K = map(int,input().split())
INF = 2147000000

# ✨ dijkstra 함수
def dijkstra(N,K):
    dist = [INF]*(100001)
    dist[N] =0
    hq = []
    heapq.heappush(hq,(0,N))
    while hq:
        w,n = heapq.heappop(hq)
        #주 목
        for nx in [(n+1,1),(n-1,1),(n*2,0)]:
            if 0<=nx[0]<100001 and dist[nx[0]] > w + nx[1]:
                dist[nx[0]] = w + nx[1]
                heapq.heappush(hq,(dist[nx[0]],nx[0]))
    print(dist[K])
dijkstra(N,K)


INF = int(1e9)
n, k = map(int, input().split())
q = []


