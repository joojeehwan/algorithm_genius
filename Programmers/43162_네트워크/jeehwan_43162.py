# from collections import deque

# def bfs(root, visited, computers):
#     visited[root] = True #방문처리
#     q = deque() #큐 생성
#     q.append((root)) # 초기값 생성
#     while q:
#         now = q.popleft() #값 빼고
#         for i in range(len(computers)): #그 값을 검증
#             #방문하지 않은 컴퓨터가 있고, 방문하지 않은 곳 이라면,
#             if computers[now][i] and not visited[i]:
#                 visited[i] = True
#                 q.append(i) # 갈 수 있으니 큐에 넣은 것!


# def solution(n, computers):
#     answer = 0 #네트워크의 갯수
#     visited = [False] * n #방문여부 확인

#     #각 점마다 확인해야 하기 때문에!
#     for i in range(n): #전체 노드를 확인하기 위해서 / for를 사용했기 떄문에 자연스럽게 i를 늘려가면서 노드를 이동할 수 있네!
#         if not visited[i]: #아직 방문하지 않은 정점이면
#             bfs(i, visited, computers) #드가자!
#             answer += 1 #하나의 네트워크를 찾았다
#     return answer


# 1. bfs풀이

from collections import deque


def bfs(start, visited, computers, n):
    # 큐 생성 / 초기값 넣기 /체크배열 체크
    q = deque([start])  # 왜 []이거는 되고 ()는 안돼,,,????
    visited[start] = True

    # bfs시작
    while q:
        now_point = q.popleft()
        for next_point in range(n):
            if computers[now_point][next_point] and not visited[next_point]:
                visited[next_point] = True
                q.append(next_point)


# 2. dfs 풀이

def dfs(lev, visited, computers):
    visited[lev] = True

    for next_point in range(len(computers)):
        if computers[lev][next_point] and not visited[next_point]:
            dfs(next_point, visited, computers)


def solution(n, computers):
    answer = 0

    visited = [False] * n

    for i in range(n):
        if not visited[i]:
            bfs(i, visited, computers, n)
            # dfs(i, visited, computers)
            answer += 1

    return answer




