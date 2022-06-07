def solution(n, edge):
    graph = [[] for _ in range(n+1)]
    for e in edge:
        graph[e[0]].append(e[1])
        graph[e[1]].append(e[0])

    check = [0] * (n+1)
    check[1] = 1
    q = []
    q.append(1)

    # bfs로 1번 노드로부터의 거리를 모두 기록
    while q:

        now = q.pop(0)

        for next in graph[now]:
            if check[next]:
                continue

            check[next] = check[now] + 1
            q.append(next)

    # 최대 거리의 노드 개수 반환
    val = max(check)
    return check.count(val)
