'''

트리란?!

1. 사이클이 없는 무방향 그래프
2. 어떤 두 노드를 선택해도, 둘 사이에 경로가 항상 하나만 존재

* 트리의 지름 구하는 방법

<정의>

1. 트리에서 임의의 정점 x를 잡는다.

2. 정점 x에서 가장 먼 정점 y를 찾는다.

3. 정점 y에서 가장 먼 정점 z를 찾는다.

=> 트리의 지름은 정점 y와 정점 z를 연결하는 경로다.


'''

import sys
sys.setrecursionlimit(int(1e5))

N = int(input())

#초기입력

#트리 전체를 담을 MAP, 노드는 1번 부터 시작한다. 그래서 N + 1을 함.
MAP = [[] for _ in range(N + 1)]

for _ in range(N - 1):

    frm, to, value = map(int, input().split())
    MAP[frm].append((to, value))
    MAP[to].append((frm, value))


#임의 점에서, 해당 노드까지의 거리를 담을 배열
visited = [-1] * (N + 1)

#트리 전체를 탐색하면서, 임의 점으로부터 해당 노드까지의 거리를 visited배열에 기록함.
def dfs(initNode, initValue):

    for nextNode, value in MAP[initNode] :

        if visited[nextNode] == -1 :
            visited[nextNode] = value + initValue
            dfs(nextNode, value + initValue)


visited[1] = 0
dfs(1, 0)
MAX_idx = 0

#가장 큰 값의 index 구하기
for index in range(len(visited)):

    if visited[MAX_idx] <= visited[index] :
        MAX_idx = index

visited = [-1] * (N + 1)
visited[MAX_idx] = 0
dfs(MAX_idx, 0)


print(visited[visited.index(max(visited))])



#bfs로도 풀어보기


from collections import deque

N = int(input())

#초기입력

#트리 전체를 담을 MAP, 노드는 1번 부터 시작한다. 그래서 N + 1을 함.
MAP = [[] for _ in range(N + 1)]

for _ in range(N - 1):

    frm, to, value = map(int, input().split())
    MAP[frm].append((to, value))
    MAP[to].append((frm, value))

visited = [False] * (N + 1)
MAX_NODE = 0
MAX_VALUE = 0
def bfs(startNode) :

    global MAX_NODE, MAX_VALUE
    visited = [False] * (N + 1)
    #큐생성 -> 초기값 입력
    q = deque()
    q.append((startNode, 0))
    visited[startNode] = True
    #bfs 시작
    while q :
        #큐에서 노드 꺼내
        nowNode, nowValue = q.popleft()

        #위에서 꺼낸 노드 기준, 갈 수 있는 곳 다 검색
        for nextNode, nextValue in MAP[nowNode]:

            #방문 여부 체크 (반복해서 가지 않아)
            if not visited[nextNode] :

                visited[nextNode] = True
                q.append((nextNode, nowValue + nextValue))

                if MAX_VALUE < (nowValue + nextValue ) :
                    MAX_VALUE = (nowValue + nextValue)
                    MAX_NODE = nextNode
    return MAX_VALUE, MAX_NODE


_, start = bfs(1)
#visited = [False] * (N + 1)  visted배열도 bfs 안에 두면, 굳이 초기화 할 필요가 없다.
print(bfs(start)[0])





