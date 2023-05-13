'''

네트워크 연결


최소신장트리

신장트리?! 하나의 그래프가 있을 떄, 모든 노드를 포함하면서 즉, 모든 노드들 간에 서로 연결은 되어있되 사이클이
존재하지 않는 '부분'그래프

이중에서, 노드들 간의 간선의 비용이 최소가 되도록 해, 만든 신장트리를 최소 신장트리라 한다.


'''



# 1. 크루스칼 알고리즘(무방향 그래프에서 사용)
# 간선 중심

#초기 입력값 vertex , edge
v = int(input())

e = int(input())

#부모 테이블 초기화
parent = [0] * (v + 1)

#0번 노드는 없으니, 1 - (v + 1)로 반복 진행 및 초기화
for i in range(1, v + 1):
    parent[i] = i


# find 연산 -> 해당 노드의 부모노드를 탐색
def find(parent, node) :

    # 처음에 자기자신으로 부모노드를 초기화 했는데, 그 값이 다르다>?!
    # 다른 부모노드가 존재한다.
    # 재귀를 통해, 부모노드를 찾아 따라간다.
    if parent[node] != node:
        parent[node] = find(parent, parent[node])

    return parent[node]

'''
이런식으로도 작성 가능. 
def find(parent, x):
	if parent[x] == x:
    	return x
    parent[x] = find(parent, parent[x])
    return parent[x]
'''

#union 연산 -> 두 노드 묶어주기
def union(parent, nodeA, nodeB) :
    nodeA = find(parent, nodeA)
    nodeB = find(parent, nodeB)

    if nodeA <  nodeB:
        parent[nodeB] = nodeA

    else:
        parent[nodeA] = nodeB


edges = []
totalCost = 0
#간선 정보 초기화
for _ in range(e) :

    frm, to, cost = map(int, input().split())
    #가중치를 기준으로 오름차순 정렬하기 위해, 첫번쨰 원소로 함.
    edges.append((cost, frm, to))

#오름차순 정렬
edges.sort()


#간선의 정보들을 하나씩 확인하면서, 크루스칼 알고리즘 진행

for i in range(e):
    cost, frm , to = edges[i]

    #사이클이 발생 안했을 때, 최소신장 트리에 포함시키기
    if find(parent, frm) != find(parent, to):
        union(parent, frm, to)
        totalCost += cost

print(totalCost)

# 2. 프림 알고리즘
# 노드 중심

import heapq

v = int(input())

e = int(input())


MAP = [[] for _ in range(v + 1)]
visited = [False for _ in range(v + 1)]
totalCost = 0

#현재 바라보고 있는 노드에서 갈 수 있는 다른 노드들을 (비용, 다음 노드) 인접리스트 형태 정리
for i in range(e):
    frm, to, cost = map(int, input().split())
    MAP[frm].append((cost, to))
    MAP[to].append((cost, frm))


q = []
#1번 노드 부터 시작함. 시작노드이기에 간선의 가중치는 0이 된다.
heapq.heappush(q, (0,1))

while q:

    cost, now_node = heapq.heappop(q)
    # 이미 방문했던 적이 없어야한다. => 방문한적이 있다면, 계산에 이미 포함된 경우이기에
    if not visited[now_node]:
        visited[now_node] = True
        totalCost += cost

        #해당 노드에서 그 다음 노드로 갈 수 있는 그래프 최소힙에 넣기
        for next_cost, next_node in MAP[now_node] :
            heapq.heappush(q, (next_cost, next_node))



print(totalCost)
