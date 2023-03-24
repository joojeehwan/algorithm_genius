'''


다익스트라 기초 다시 공부


'''
import heapq
import math

INF = math.inf

#시작노드 입력 및 간선의 갯수 입력
n, m = map(int, input().split())

#시작 노드 입력받기
start_node = int(input())

#최단거리 테이블
distance = [INF] * (n + 1)

#노드 연결 정보
MAP = [[] for _ in range(n + 1)]

# 간선(노드와 노드의 연결)의 갯수 만큼 반복이 이루어지겠지
for _ in range(m) :
    frm, to , cost = map(int, input().split())
    MAP[frm].append((to, cost))


#다익스트라에서 최소힙을 사용하는 이유?! 최단거리 테이블에서 거리 갱신 이후에, 가장 작은 값을 pop 하기 위함.

def dijkstra(startNode):
    
    
    q = []
    #최소힙에,시작 노드 설정  (시작점에서 해당 노드까지 이동하는데 드는 비용, 해당 노드 번호)
    heapq.heappush(q, (0, startNode))

    #시작노드의 경우 "최단거리"가 0이다.
    distance[startNode] = 0

    while q :

        dist, now = heapq.heappop(q) #최소힙에서 값을 하나씩 꺼내기

        # 가지치기 1
        # 기존에 여기 까지 오는데 오는 거리보다, 현재 위치에서 다음 노드로 가는 거리가 더 긴곳?!
        # 굳이 가보지 않아도 된다. 우리는 최단 거리를 구하고 있기 때문에
        if distance[now] < dist :
            continue

        # 이제 해당 노드를 거쳐서 다음 더 최단거리를 구하는 로직 시작

        for next_node_number, next_node_cost in MAP[now] :
            cost = dist + next_node_cost # 해당 노드를 거쳐서 갈 떄 거리

            #선택된 노드를 거쳐서 가는 것이 현재 가는 거리보다 더 작을 떄만 값을 갱신
            if cost < distance[next_node_number] :
                distance[next_node_number] = cost
                heapq.heappust(q, (cost, next_node_number))

dijkstra(start_node)

# 모든 노드로 가기 위한 최단 거리를 출력
for i in range(1, n+1):
  # 도달할 수 없는 경우
  if distance[i] == INF:
    print("infinity")
  else:
    print(distance[i])



'''


2가지 case로 분기.

1. 환승을 하지 않고 그냥 가는 경우 

2. 환승해서 가능 경우 

1, 2 case중에 더 작은 경우를 출력


다익스트라 함수를 만들어. 시작노드에서 도착노드까지의 최단거리를 계산
'''

import heapq
import math

def dijkstra(start_node, goal_node, N ,MAP) :

    #최소힙 (비용, 노드)
    q = []
    heapq.heappush(q, (0, start_node))

    #최단거리 배열 초기화
    distance = [math.inf] * (N + 1)
    distance[start_node] = 0

    while q :

        dist, now = heapq.heappop(q)

        if distance[now] < dist:
            continue
        
        #거쳐가기 시작해보자
        for next_node_number, next_node_cost in MAP[now]:

            cost = dist + next_node_cost

            if cost < distance[next_node_number]:
                distance[next_node_number] = cost
                heapq.heappush(q, (cost, next_node_number))

    return distance[goal_node]

def solution(n, s, a, b, fares):

    answer = 0

    #초기 MAP 초기화
    MAP = [[] for _ in range(n + 1)]

    # 양방향인 것 인지.
    # (노드번호, 비용)
    for fare in fares :
        frm, to, cost = fare
        MAP[frm].append((to, cost))
        MAP[to].append((frm, cost))

    #case1 - 합승x
    answer = dijkstra(s, a, n, MAP) + dijkstra(s, b, n, MAP)

    #case2 - 합승0
    for i in range(1, n + 1):

        # s(start)가 i가 되는 경우, case1의 경우과 마찬가지로 합승하지 않고,
        # 시작지점에서부터 각자의 집 까지 따로 가는 경우가 되어버린다.
        if s != i :
            answer = min(answer, dijkstra(s, i, n, MAP) + dijkstra(i, a, n, MAP) + dijkstra(i, b, n, MAP))

    return answer


