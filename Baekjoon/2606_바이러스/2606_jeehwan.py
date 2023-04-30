'''

연결되어 있느 노드들의 갯수를 구하라

1번 컴퓨터가 바이러스에 걸렸을 때, 바이러스에 걸리는 수를 구하라.
'''


from collections import deque

#입력은 인접행렬 방식


computerCnt = int(input())

edge = int(input())

MAP = [[] for _ in range(computerCnt + 1)]

ans = 0

for _ in range(edge):

    frm , to = map(int, input().split())
    MAP[frm].append(to)
    MAP[to].append(frm)


def bfs(nodeIndex, ans) :

    q = deque()
    q.append((nodeIndex))
    visited = [False] * (computerCnt + 1)
    visited[nodeIndex] = True

    while q :

        now_node = q.popleft()

        for next_node in MAP[now_node] :

            #한번 간 곳은 가지 않는다
            if not visited[next_node]:
                q.append((next_node))
                visited[next_node] = True
                ans += 1

    return ans


print(bfs(1, ans))