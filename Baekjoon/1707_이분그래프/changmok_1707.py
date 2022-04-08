import sys
from collections import deque

# 재미난 색칠 공부
# 첫 시작을 1로 칠하고, 번갈아가면서 2, 1, 2, 1...로 칠하되
# 다음에 갈 노드에 이미 칠할 색이 아닌 다른 색이 있으면
# NO 리턴하면서 탈출하는 solution() 함수를 이용

input = sys.stdin.readline

def solution():
    v, e = map(int, input().split())
    graph = [[] for _ in range(v+1)]
    for _ in range(e):
        t, u = map(int, input().split())
        graph[t].append(u)
        graph[u].append(t)
    visit = [False] * (v+1)
    p = [0] * (v+1)
    m = [0, 2, 1]
    while not all(visit[1:]):
        start = visit[1:].index(False) + 1
        visit[start] = True
        p[start] = 1
        q = deque([(start, 1)])
        while q:
            node, party = q.popleft()
            for next in graph[node]:
                if p[next] == party:
                    return "NO"
                if visit[next]:
                    continue
                q.append((next, m[party]))
                visit[next] = True
                p[next] = m[party]
    return "YES"

for k in range(int(input())):
    print(solution())