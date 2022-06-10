# def solution(m, n, puddles):
#     #1 부터 시작하는 (1,1) ~ (n, m) 2차원 배열
#     memo = [[0 for _ in range(m + 1)] for _ in range(n+1)] # 0으로 초기화

#     for col, row in puddles:
#         memo[row][col] = -1 #갈 수 없는 물 웅덩이 표시
#     memo[1][1] = 1 #출발 지점 1로 지정
#     def dp(row, col):
#         #물 웅덩이 이거나, 범위 밖에 있는 것
#         if row < 1 or col < 1 or memo[row][col] < 0 :
#             return 0
#         #이미 계산한 값이 있으면 값을 바로 가져옴
#         if memo[row][col] > 0 :
#             return memo[row][col]

#         memo[row][col] = dp(row, col - 1) + dp(row-1, col)
#         return memo[row][col]
#     return dp(n, m) % 1000000007

# bfs 풀이

dr = [0, 1]
dc = [1, 0]

from collections import deque


def solution(m, n, puddles):
    answer = 0
    # . 1. 맵 구성
    MAP = [[0] * m for _ in range(n)]
    MAP[0][0] = 1
    # 2. 초기값 구성
    q = deque([(0, 0)])
    while q:
        row, col = q.popleft()
        for i in range(2):
            next_row = row + dr[i]
            next_col = col + dc[i]

            # 범위 안에 있는 녀석
            if 0 <= next_row < n and 0 <= next_col < m:
                # 그러면서 웅덩이가 아닌 것!
                # 웅덩이 안에 이 안의 좌표가 있다면!을 이런식으로 작성하네 굿,,!
                if [next_col + 1, next_row + 1] in puddles:
                    continue

                MAP[next_row][next_col] += MAP[row][col]
                if (next_row, next_col) not in q:
                    q.append((next_row, next_col))
    answer = MAP[n - 1][m - 1] % 1000000007
    return answer