'''

LCA

나동빈 동영상 참고

'''

import sys
sys.setrecursionlimit(1e9)

n = int(input())
parent = [0] * (n + 1)      # 각 노드의 부모 노드 정보
d = [0] * (n + 1)           # 각 노드까지의 깊이
visited = [0] * (n + 1)     # 방문 여부
graph = [[] for _ in range(n + 1)]

for _ in range(n - 1):
    a, b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)


# 루트 노드부터의 깊이 구하기
def dfs(x, depth):
    visited[x] = True
    d[x] = depth

    for node in graph[x]:
        #이미 방문한 곳은 가지 않는다.
        if visited[node]:
            continue
        #현재 레벨을 부모리스트에 기록 => 부모 노드 정보 기록
        parent[node] = x
        #재귀
        dfs(node, depth + 1)


# 최소 공통 조상 찾기
def lca(a, b):
    # 깊이 맞추기 => 같은 레벨의 깊이에서 시작할 수 있도록
    while d[a] != d[b]:
        if d[a] > d[b]:
            #부모 쪽으로 한칸 이동
            a = parent[a]
        else:
            b = parent[b]

    # 노드 맞추기 => 공통 조상을 찾을 떄까지, 부모 방향으로 동시에 이동
    while a != b:
        a = parent[a]
        b = parent[b]

    return a


dfs(1, 0)

m = int(input())

for _ in range(m):
    a, b = map(int, input().split())
    print(lca(a, b))


