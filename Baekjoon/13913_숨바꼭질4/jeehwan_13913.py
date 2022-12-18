
'''

기본 bfs에 경로를 추가하는 방법

1. path를 넣어서, 그 길을 기록

2. 경로를 구하는 함수 구하기

'''

from collections import deque


def findPath(node):

    lst = []
    temp = node

    for _ in range(visited[node] + 1):
        lst.append(temp)
        temp = path[temp]
    # 배열안에 있는 값들을 역순으로 꺼내, 문자열로 만들고, 이를 공백기준으로 합친다.
    print(" ".join(map(str, lst[::-1])))

def bfs() :

    q = deque()
    q.append((n))
    #visited[n] = 1 이 차이를 알아야 한다..

    while q :

        now_node = q.popleft()

        if now_node == k:
            print(visited[now_node])
            findPath(now_node)
            return

        for next_node in (now_node - 1, now_node + 1, now_node * 2):

            if 0 <= next_node < 100001 and visited[next_node] == 0:
                q.append((next_node))
                visited[next_node] = visited[now_node] + 1
                path[next_node] = now_node

n, k = map(int, input().split())

visited = [0] * 100001
path = [0] * 100001
bfs()

