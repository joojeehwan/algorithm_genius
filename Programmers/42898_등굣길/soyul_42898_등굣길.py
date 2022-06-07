def solution(m, n, puddles):

    dp = [[0] * m for _ in range(n)]
    dp[0][0] = 1

    for j in range(1, m):              # 맨 윗줄 먼저 채우기
        if [j+1, 1] in puddles:        # 웅덩이면 0으로
            dp[0][j] = 0
            continue
        dp[0][j] += dp[0][j-1]

    for i in range(1, n):               # 맨 왼쪽줄 먼저 채우기
        if [1, i+1] in puddles:         # 웅덩이면 0
            dp[i][0] = 0
            continue
        dp[i][0] += dp[i-1][0]

    for i in range(1, n):
        for j in range(1, m):
            if [j+1, i+1] in puddles:           # 웅덩이면 패스
                continue
            dp[i][j] = dp[i-1][j] + dp[i][j-1]

    answer = dp[-1][-1]
    return answer % (1000000007)

"""
bfs로 풀었더니 시간초과!

from collections import deque

def bfs(m, n, puddles):

    di = [0, 1]     # 오른쪽, 아래
    dj = [1, 0]

    q = deque()
    q.append((0, 0))

    result = 0

    while q:
        now_i, now_j = q.popleft()

        for k in range(2):
            next_i = now_i + di[k]
            next_j = now_j + dj[k]

            if next_i == n-1 and next_j == m-1:
                result += 1
                continue

            if next_i >= n or next_j >= m:          # 범위 넘어가면 pass
                continue
            if [next_j+1, next_i+1] in puddles:        # 웅덩이면 pass
                continue

            q.append((next_i, next_j))

    return result

def solution(m, n, puddles):


    answer = bfs(m, n, puddles)
    return answer % (1000000007)


print(solution(4, 3, [[2, 2]]))

"""