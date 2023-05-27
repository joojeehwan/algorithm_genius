''''


2개의 노드를 정해서, 해당 노드에서 그 다음 노드까지의 거리가

가중치 = 길이
가장 긴것을 찾아라



1. 한개의 노드 기준으로, 다른 제외한 다른 노드들을 탐색(dfs)

2. maxCnt 변수 생성해, 최대값을 갱신


지름 2개의 노드 구하는 방법

1. 트리에서 임의의 정점 x를 잡는다.

2. 정점 x에서 가장 먼 정점 y를 찾는다.

3. 정점 y에서 가장 먼 정점 z를 찾는다.

트리의 지름은 정점 y와 정점 z를 연결하는 경로다.



'''


#처음 내 생각

# n = int(input())
#
# MAP = [[] * n for _ in range(n)]
#
# maxCnt = 0
#
# for _ in range(n):
#     parent, child, value = map(int, input().split())
#     MAP[parent].append((child, value))
#
#
# def dfs(MAP, start, visited):
#     global maxCnt
#
#     visited.append(start)
#
#     for node, value in MAP :
#         if node not in visited:
#             maxCnt += value
#             dfs(MAP, node, visited)



import sys

sys.setrecursionlimit(1e9)


def dfs(parent, Pvalue):

    for child, Cval in MAP[parent]:

        # 가지 않은 곳
        if visited[child] ==  -1:
            visited[child] = Pvalue + Cval
            dfs(child, Pvalue + Cval)


N = int(input())

MAP = [[] for _ in range(N + 1)]

for _ in range(N - 1):
    parent, child, value = map(int, input().split())
    MAP[parent].append((child, value))
    MAP[child].append((parent, value))


visited = [-1] * (N + 1) #1차원 배열이지, 그냥 각각의 노드들 가고, 안가고 설정하는 건데
visited[1] = 0
dfs(1, 0)

start = visited.index(max(visited))

visited = [-1] * (N + 1)
visited[start] = 0
dfs(start, 0)

print(max(visited))

# BFS
from collections import deque

max_node = -1


def bfs(start_node):
    global n, max_node
    visited = [False] * (n + 1)
    que = deque([[start_node, 0]])
    visited[start_node] = True
    max_dist = 0

    while que:
        now, now_dist = que.popleft()
        for child, child_dist in data[now]:
            if not visited[child]:
                visited[child] = True
                que.append([child, now_dist + child_dist])
                if max_dist < now_dist + child_dist:
                    max_dist = now_dist + child_dist
                    max_node = child
    return max_dist


n = int(input())
if n == 1:
    print(0)
else:
    data = [[] for _ in range(n + 1)]
    for _ in range(n - 1):
        # 부모, 자식, 거리
        a, b, c = map(int, input().split())
        data[a].append([b, c])
        data[b].append([a, c])
    bfs(1)
    print(bfs(max_node))