import heapq


def solution(N, road, K):
    answer = 1  # 본인 포함
    dist = [[500001] * (N+1) for _ in range(N+1)]  # 거리의 최대값이 50만이어서 그걸 넘는 수로 인접 행렬초기화
    connect_to_1 = []  # heap이 될 list

    for town1, town2, distance in road:
        distance = min(dist[town1][town2], distance)  # 한 마을간 거리가 2개 이상인 경우
        dist[town1][town2] = distance
        dist[town2][town1] = distance
        # town1과 town2가 정렬이 되어있다는 보장이 없는 것 같아서
        if town1 == 1:
            heapq.heappush(connect_to_1, (distance, town2))
        if town2 == 1:
            heapq.heappush(connect_to_1, (distance, town1))

    while connect_to_1:
        # 1과 연결된 마을중 가장 가까운 마을 번호를 뽑아서
        connect = heapq.heappop(connect_to_1)[1]

        # 원래는 connect와 연결된 곳만 봐야하지만 마을이 50개밖에 안되니까 걍 다 돌아도 된다고 생각함
        # 연결 정보를 위해 메모리를 또 쓰고싶지 않았음
        for town in range(2, N+1):
            if dist[connect][town] < 500001:  # connect와 연결된 마을 중
                if dist[1][town] > dist[1][connect] + dist[connect][town]:
                    dist[1][town] = dist[1][connect] + dist[connect][town]  # 더 최소인 경우에 업데이트하고
                    heapq.heappush(connect_to_1, (dist[1][town], town))
                    # 그렇게 연결된 마을을 또 connect_1에 저장해 여러 다리를 건너서 계산할 수 있게끔 했다.

    for distance_to_1 in dist[1]:
        if distance_to_1 <= K:
            answer += 1

    return answer


print(solution(6, [[1,2,1],[1,3,2],[2,3,2],[3,4,3],[3,5,1],[3,5,3],[5,6,1]], 4))

"""
결과
테스트 1 〉	통과 (0.02ms, 10.4MB)
테스트 2 〉	통과 (0.02ms, 10.3MB)
테스트 3 〉	통과 (0.02ms, 10.3MB)
테스트 4 〉	통과 (0.04ms, 10.3MB)
테스트 5 〉	통과 (0.04ms, 10.3MB)
테스트 6 〉	통과 (0.02ms, 10.3MB)
테스트 7 〉	통과 (0.03ms, 10.4MB)
테스트 8 〉	통과 (0.04ms, 10.2MB)
테스트 9 〉	통과 (0.02ms, 10.3MB)
테스트 10 〉	통과 (0.03ms, 10.4MB)
테스트 11 〉	통과 (0.03ms, 10.4MB)
테스트 12 〉	통과 (0.13ms, 10.3MB)
테스트 13 〉	통과 (0.09ms, 10.3MB)
테스트 14 〉	통과 (1.13ms, 10.3MB)
테스트 15 〉	통과 (1.68ms, 10.3MB)
테스트 16 〉	통과 (0.05ms, 10.3MB)
테스트 17 〉	통과 (0.09ms, 10.2MB)
테스트 18 〉	통과 (0.51ms, 10.2MB)
테스트 19 〉	통과 (1.54ms, 10.4MB)
테스트 20 〉	통과 (0.69ms, 10.3MB)
테스트 21 〉	통과 (1.56ms, 10.4MB)
테스트 22 〉	통과 (0.64ms, 10.3MB)
테스트 23 〉	통과 (1.74ms, 10.4MB)
테스트 24 〉	통과 (1.30ms, 10.5MB)
테스트 25 〉	통과 (2.39ms, 10.6MB)
테스트 26 〉	통과 (1.97ms, 10.5MB)
테스트 27 〉	통과 (2.00ms, 10.4MB)
테스트 28 〉	통과 (2.30ms, 10.5MB)
테스트 29 〉	통과 (2.23ms, 10.6MB)
테스트 30 〉	통과 (1.33ms, 10.6MB)
테스트 31 〉	통과 (0.20ms, 10.4MB)
테스트 32 〉	통과 (0.23ms, 10.3MB)
"""