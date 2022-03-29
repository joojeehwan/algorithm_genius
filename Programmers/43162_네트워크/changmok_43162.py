from collections import deque

def solution(n, computers):
    networked = [False] * n # 컴퓨터 체크 배열
    answer = 0
    
    # 컴퓨터 배열을 처음부터 끝까지 순회하며
    # 네트워크에 속하지 않은 컴퓨터가 있는 경우 bfs 탐색
    for start in range(n):

        # 만약 체크가 되지 않은 새로운 시작점이라면
        if not networked[start]:

            answer += 1 # 네트워크 갯수 추가
            networked[start] = True # 시작점 체크 처리
            q = deque([start]) # bfs 용 큐 선언 및 초기화

            while q: # bfs 시작
                node = q.popleft()
                for nxi in range(n): # 해당 컴퓨터에 대하여
                    if computers[node][nxi] and not networked[nxi]: # 다른 컴퓨터가 연결되어 있고, 네트워크에 속해있지 않다면
                        networked[node] = True
                        q.append(nxi)
    
    return answer