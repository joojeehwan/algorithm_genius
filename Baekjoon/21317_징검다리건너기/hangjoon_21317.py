rocks = int(input())  # 돌의 개수
s_jumps, l_jumps = [0] * (rocks - 1), [0] * (rocks - 1)
for _ in range(rocks - 1):
    s_jumps[_], l_jumps[_] = map(int, input().split())  # 작은 점프, 큰 점프
ll_jump = int(input())  # 매우 큰 점프

# DP
dp = [123456789] * rocks  # 최대값으로 초기화한 dp 배열
dp[0] = 0

# 작은 점프 + 큰 점프 최소 에너지 구하기
for i in range(rocks - 1):
    # 작은 점프 되는지
    if i + 1 < rocks:
        dp[i + 1] = min(dp[i + 1], dp[i] + s_jumps[i])
    # 큰 점프 되는지
    if i + 2 < rocks:
        dp[i + 2] = min(dp[i + 2], dp[i] + l_jumps[i])

# 매우 큰 점프 최소 에너지 구하기
ans = dp[-1]
for j in range(rocks - 3):  # 매우 큰 점프를 넣어보고 계산할 위치
    n_dp = dp[:]
    n_dp[j + 3] = dp[j] + ll_jump
    for k in range(j + 3, rocks - 1):
        # 작은 점프 되는지
        if k + 1 < rocks:
            n_dp[k + 1] = min(n_dp[k + 1], n_dp[k] + s_jumps[k])
        # 큰 점프 되는지
        if k + 2 < rocks:
            n_dp[k + 2] = min(n_dp[k + 2], n_dp[k] + l_jumps[k])
    # 기존 dp와 비교
    ans = min(ans, n_dp[-1])
print(ans)
