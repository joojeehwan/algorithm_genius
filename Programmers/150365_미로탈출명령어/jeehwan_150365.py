'''

다익스트라

1. 출발 노드를 설정한다

2. 최단거리 테이블을 초기화한다.

-> 다른 모든 노드로 가는 최단거리를 '무한'으로 초기화한다

3. 방문하지 않은 노드 중에서 최단거리가 가장 짧은 노드를 선택한다.

-> 이때 선택된 노드의 최단거리는 확정된다.

4. 해당 노드를 거쳐 다른 노드로 가는 비용를 게산하여 최단 거리 테이블을 갱신한다.

5. 3~4 과정을 반복한다.




DP + 다익스트라


2차원 DP 배열 = 정점 * 현재까지의 총 비용

=> DP[V][C] : C 비용을 들였을 때, V정점까지 가기 위한 최소한의거리


'''
import heapq

INF = float('inf')
for _ in range(int(input())):
    n,cost,m = map(int,input().split())
    dp = [[INF]*(n) for _ in range(cost+1)]
    graph = [[] for i in range(n)]

    for i in range(m):
        u,v,c,d = map(int,input().split())
        u-=1;v-=1
        graph[u].append((v,c,d))

    heap = [(0,0,0)] # dist,cost,node
    while(heap):
        curDist,curCost,curNode = heapq.heappop(heap)
        if curDist > dp[curCost][curNode]:
            continue

        for toNode,toCost,toDist in graph[curNode]:
            d = curDist + toDist
            c = curCost + toCost
            if c <= cost and d < dp[c][toNode]:
                # 더 높은 cost를 투자할 때의 가중치도 맞춰준다.
                for i in range(c,cost+1):
                    if dp[i][toNode] > d:
                        dp[i][toNode] = d
                    else:
                        break
                heapq.heappush(heap,(d,c,toNode))

    print(dp[cost][n-1] if dp[cost][n-1] != INF else "Poor KCM")
