import heapq

def solution(N, road, K):

    adj = [[] for _ in range(N+1)]
    for n1, n2, w in road:
        adj[n1].append((w, n2))
        adj[n2].append((w, n1))

    def dijkstra(start):
        INF = 1e9
        dist = [INF] * (N + 1)
        dist[start] = 0

        hq = []
        heapq.heappush(hq, (0, start))

        while hq:
            now_cost, now = heapq.heappop(hq)

            for cost, to in adj[now]:
                if now_cost + cost < dist[to]:
                    dist[to] = now_cost + cost
                    heapq.heappush(hq, (dist[to], to))

        return dist

    result = dijkstra(1)

    answer = 0
    for cost in result:
        if cost <= K:
            answer += 1

    return answer
