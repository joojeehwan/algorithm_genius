from collections import deque

def solution(n, edge):
    answer = 0
    
    graph = [[] for _ in range(n+1)]
    dist = [-1] * (n+1)
    dist[1] = 0
    furthest = 0
    for v1, v2 in edge:
        graph[v1].append(v2)
        graph[v2].append(v1)
    
    q = deque([1])
    while q:
        v = q.popleft()
        for nv in graph[v]:
            if -1 != dist[nv] and dist[v]+1 >= dist[nv]:
                continue
            dist[nv] = dist[v] + 1
            furthest = max(furthest, dist[nv])
            q.append(nv)
    
    for d in dist:
        if furthest == d:
            answer += 1
    return answer