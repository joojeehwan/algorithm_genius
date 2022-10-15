"""
https://hbj0209.tistory.com/170

100줄 가까이 쓰고 5시간 넘게 걸려도 틀려서 포기
왜 답은 이렇게 간단하지? 왜 이게 정답이지??
난 무슨 헛짓거릴 한걸까......
"""

import heapq


def solution(n, s, a, b, fares):

    def dijkstar(start):
        from_start = [100001 for _ in range(n+1)]  # start에서부터의 최단 거리?
        from_start[start] = 0

        q = []
        heapq.heappush(q, (from_start[start], start))  # 자기 자신부터?

        while q:
            dist_start_spot, spot = heapq.heappop(q)
            # spot(중간지점)과 연결된 장소들
            for connect, dist_spot_connect in graph[spot]:
                # 현재 start과 도착지(connect)까지의 거리가  start ~ spot + spot ~ connect 까지의 거리보다 멀다면
                if from_start[connect] > dist_start_spot + dist_spot_connect:
                    # 더 적은 값으로 갱신해주고
                    from_start[connect] = dist_start_spot + dist_spot_connect
                    # 연결된 부분이므로 heap에 넣어준다.
                    heapq.heappush(q, ([from_start[connect], connect]))

        return from_start

    answer = 1000001

    graph = [[] for _ in range(n+1)]

    for spot1, spot2, distance in fares:
        graph[spot1].append((spot2, distance))
        graph[spot2].append((spot1, distance))

    dist = [[]]  # index 0 때문에
    for i in range(1, n+1):
        dist.append(dijkstar(i))  # 한 정점씩 시작 지점으로 설정해보면서 최단 거리를 구해본다.

    for start in range(1, n+1):
        answer = min(answer, dist[s][start] + dist[start][a] + dist[start][b])

    return answer


print(solution(6,1,4,6,[[1, 2, 8], [1, 3, 9], [1, 4, 10], [4, 5, 2], [5, 6, 5]]))
# print(solution(7,3,4,1,[[5, 7, 9], [4, 6, 4], [3, 6, 1], [3, 2, 3], [2, 1, 6]]))
# print(solution(6,4,5,6,[[2,6,6], [6,3,7], [4,6,7], [6,5,11], [2,5,12], [5,3,20], [2,4,8], [4,3,9]]))