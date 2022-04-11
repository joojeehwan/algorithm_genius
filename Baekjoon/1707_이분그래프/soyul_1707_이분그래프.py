import sys

def bfs(i):

    q = []
    q.append(i)
    visited[i] = 1
    while q:
        now = q.pop(0)

        for next in graph[now]:
            if not visited[next]:           # 방문한 곳이면 패스
                q.append(next)
                visited[next] = visited[now] + 1
            if visited[next] % 2 == visited[now] % 2:                   # 같은 그룹이면 바로 1 리턴
                return 1
    return 0

k = int(sys.stdin.readline())
for _ in range(k):
    V, E = map(int, sys.stdin.readline().split())

    # 그래프 표시
    graph = [[] for _ in range(V + 1)]
    for _ in range(E):
        u, v = map(int, sys.stdin.readline().split())
        graph[u].append(v)
        graph[v].append(u)

    flag = 0
    visited = [0] * (V + 1)
    for i in range(1, V + 1):           # 방문 안한곳 bfs 실행
        if visited[i]:
            continue
        if bfs(i):
            flag = 1
            break
    if flag:
        print('NO')
    else:
        print('YES')