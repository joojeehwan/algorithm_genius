def solution(triangle):

    dp = [[0] * len(triangle) for _ in range(len(triangle))]

    dp[0][0] = triangle[0][0]                           # 맨 처음 값은 그대로 넣어줌
    for i in range(1, len(triangle)):
        dp[i][0] = dp[i-1][0] + triangle[i][0]          # 0번째 index는 이전 0번째 값이랑 바로 더함
        for j in range(1, i):                           # 중간 index는 윗줄의 값 중 최대 값과 더해줌
            dp[i][j] = max(dp[i-1][j-1], dp[i-1][j]) + triangle[i][j]   # 마지막 index는 그대로 더해줌
        dp[i][i] = dp[i-1][i-1] + triangle[i][i]

    answer = max(dp[-1])
    return answer


print(solution([[7], [3, 8], [8, 1, 0], [2, 7, 4, 4], [4, 5, 2, 6, 5]]))