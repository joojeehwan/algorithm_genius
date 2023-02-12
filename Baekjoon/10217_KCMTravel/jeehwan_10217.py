'''

다익스트라

1. 출발 노드를 설정한다

2. 최단거리 테이블을 초기화한다.

-> 다른 모든 노드로 가는 최단거리를 '무한'으로 초기화한다

3. 방문하지 않은 노드 중에서 최단거리가 가장 짧은 노드를 선택한다.

-> 이때 선택된 노드의 최단거리는 확정된다.

4. 해당 노드를 거쳐 다른 노드로 가는 비용를 게산하여 최단 거리 테이블을 갱신한다.

5. 3~4 과정을 반복한다.


'''

# 힙큐 쓴 풀이

# import heapq
# import sys

# input = sys.stdin.readline
# INF = int(1e9)
#
# # 노드의 갯수, 간선의 갯수 입력받기
# n, m = map(int, input().split())
# # 시작 노드 번호를 입력받기
# start = int(input())
# # 최단거리 테이블
# distance = [INF] * (n + 1)
#
# # 노드 연결정보
# graph = [[] for _ in range(n + 1)]
#
# for _ in range(m):
#     # frm번 노드에서 to번 노드로 가는 비용 cost
#     frm, to, c = map(int, input().split())
#     graph[frm].append((to, c))
#
#
# # 다익스트라 알고리즘!최소힙 사용! => 최단거리 테이블에서 거리 갱신 이후에 가장 작은 값을 뽑는,,!
# # 이것이 바로 자료구조를 사용하는 이유
#
# def dijkstra(start):
#     q = []
#     # 시작 노드 설정
#     heapq.heappush(q, (0, start))
#     # 시작은 당연히 거기까지 거리가 0이지!
#     distance[start] = 0
#
#     while q:
#         dist, now = heapq.heappop(q)  # 최소힙에서 꺼내! 가장 최단거리 테이블 작은애!
#
#         # 기존에 있는 거리보다 긴 곳이라면! 쳐다볼 필요도 없음.
#         # 그냥 원래 있던 길로 가면 되니!
#         if distance[now] < dist:
#             continue
#
#         # 선택된 노드의 인접한 노드들 확인
#         for i in graph[now]:
#             cost = dist + i[1]  # 해당 노드를 거쳐 갈 때 거리
#             # 선택된 노드를 거쳐서 가는것이 현재 가는 거리보다 작다면 갱신
#             if cost < distance[i[0]]:
#                 distance[i[0]] = cost
#                 heapq.heappush(q, (cost, i[0]))
#
#
# dijkstra(start)
#
# # 모든 노드로 가기 위한 최단 거리를 출력
# for i in range(1, n + 1):
#     # 도달할 수 없는 경우
#     if distance[i] == INF:
#         print("infinity")
#     else:
#         print(distance[i])

'''

DP + 다익스트라


2차원 DP 배열 = 정점 * 현재까지의 총 비용

=> DP[V][C] : C 비용을 들였을 때, V정점까지 가기 위한 '최소한'의거리


why?! 근데 DP를 활용하나?!

그냥 다익스트라를 쓸려고 하니, 어떤 것이 더 가중치가 있는지를 노드 탐색 당시에는 알 수 가 없음(다익스트라는 그리디 알고리즘 이기에 모든 탐색이 끝난 이후에, 결과를 알 수 있음)

예시) 소요시간은 짧지만 비용이 비싼 경우 // 소요 시간은 길지만 비용이 싼 경우  중에 어떤 게 더 가중치가 있는 건데?!

단순히 다익스트라로 풀게 되면, 최단거리이기에 시간이 짧은 것으로만 가게되어, '비용' 이라는 변수를 생각하지 못함

이에 DP배열을 생각해, 돈에 따른 각 정점 까지 가기 위한 최소거리를 만들어 모든 경우의 수를 생각하는 것


ex)
A    ->      B   :     MONEY 1  // TIME 5


A    ->      C   :     MONEY 5 //  TIME 1


        0 1 2 3 4 5   (돈)
    A   0
    B     5
    C             1

    ...

    n   inf  inf  inf  inf  inf  inf
  (정점)

중요! 해당 DP 배열을 왼쪽에서 오른쪽으로 방향으로 업데이트, 즉 돈이 작은 것에서부터 큰 방향으로 업데이트를 한다.
우리가 찾고 싶은 n번째에 도착했을 때, dp를 활용한 다익스트라를 통해서 해당 배열을 다 채울 텐데
n번째 행에서 기존에 주어진 '비용'을 넘지 않는 것의 값을 출력하고, 만약에 모든 값이 INF로 채워져 있다면 poor kcm을 출력

'''


# 다익스트라 풀이 1
# import heapq
#
# INF =  int(1e9)
# T = int(input())
# for _ in range(T):
#
#     n, cost, m = map(int,input().split())
#     dp = [[INF] * (n) for _ in range(cost+1)]
#     MAP = [[] for i in range(n)]
#
#     for i in range(m):
#         u, v, c, d = map(int,input().split())
#         u-=1
#         v-=1
#         MAP[u].append((v,c,d))
#
#     q = []  #[(0,0,0)[ (dist, cost, node)
#     heapq.heappush(q, (0, 0, 0))
#
#     while q :
#         curTime, curCost, curNode = heapq.heappop(q)
#
#         #같은 비용으로 더 많은 시간이 걸리는 곳은 굳이 보지도 않는다.
#         if curTime > dp[curCost][curNode]:
#             continue
#
#         #선택된 노드의 인접한 노드들 확인
#         for toNode,toCost,toTime in MAP[curNode]:
#
#             t = curTime + toTime # 해당 노드들 거쳐갈떄의 시간 및 비용 계산
#             c = curCost + toCost
#
#             # 비용이 더 같거나 작게 들면서, 시간이 더 작게 든다면 갱신
#             if c <= cost and t < dp[c][toNode]:
#                 # 더 높은 cost를 투자할 때의 가중치도 맞춰준다.
#                 for i in range(c,cost+1):
#                     if dp[i][toNode] > t:
#                         dp[i][toNode] = t
#                     else:
#                         break
#                 heapq.heappush(q,(t,c,toNode))
#
#     print(dp[cost][n-1] if dp[cost][n-1] != INF else "Poor KCM")




#dp 만을 사용한 풀이 2

import sys
import math

def solve() :

    n, m, k = map(int, sys.stdin.readline().rstrip().split())
    MAP = [[] for _ in range(n + 1)]
    for _ in range(k):
        u, v, c, d = map(int, sys.stdin.readline().rstrip().split())
        MAP[u].append((v, c, d))

    DP = [[math.inf] * (m + 1) for _ in range(n + 1)]
    #시작노드에서 시작비용이 0일때 시간도 0이다.
    DP[1][0] = 0

    for money in range(m + 1): # col, 돈이 증가하는 순서로
        for node in range(1, n + 1) : #row, 번쨰는 사용하지 않아! 1부터 시작
            if DP[node][money] != math.inf :

                for toNode, toCost, toTime in MAP[node]:
                    if money + toCost <= m : #일단 비용이 m보다 크면 볼 필요가 없다.
                        #갱신할 곳이 시간(기존 값)과 그곳을 가기 위한 node를 거쳐가게 되는 것의 시간(변경 값)을 비교해 더 작은 곳의 시간 비용으로 계산
                        DP[toNode][money + toCost] = min(DP[toNode][money + toCost], DP[node][money] + toTime)
    answer = min(DP[n])

    if answer == math.inf :
        print("Poor KCM")
    else:
        print(answer)



TC = int(input())
for _  in range(TC):
    solve()