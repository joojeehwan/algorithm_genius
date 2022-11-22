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


n = int(input())

MAP = [[] * n for _ in range(n)]

maxCnt = 0

for _ in range(n):
    parent, child, value = map(int, input().split())
    MAP[parent].append((child, value))


def dfs(MAP, start, visited):
    global maxCnt

    visited.append(start)

    for node, value in MAP :
        if node not in visited:
            maxCnt += value
            dfs(MAP, node, visited)








