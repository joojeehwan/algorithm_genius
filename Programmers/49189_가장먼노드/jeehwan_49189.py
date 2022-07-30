from collections import deque


def solution(n, edge):
    answer = 0
    MAP = [[] for _ in range(n + 1)] #연결된 노드 정보 그래프 0번 노드 사용안한다! 그래서 n + 1 작업을 하는 것!
    distance = [-1] * (n + 1) #각 노드의 최단 거리 리스트


    #1.MAP 구성 => 노드들 간의 연결, 인덱스가 출발 노드, 인덱스 안의 값들이 갈 수 잇는 노드들의 인덱스
    for e in edge:
        MAP[e[0]].append(e[1])
        MAP[e[1]].append(e[0])

    #2. 시작점 세팅
    q = deque([1])
    # q.append([1])
    distance[1] = 0 #시작 노드의 최단거리는 0으로

    #bfs 실행
    while q:
        now = q.popleft() #현재 노드

        #현재 노드에서 이동할 수 있는 모든 노드 확인
        for i in MAP[now]:
            if distance[i] == -1: #아직 방문x
                q.append(i) #큐에 추가
                distance[i] = distance[now] + 1 #최단거리 갱신

    #가장 멀리 떨어진 노드 개수 구하기
    for dis in distance:
        if dis == max(distance):
            answer += 1
    return answer