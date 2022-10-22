n = int(input())
if n == 1:
    print(0)
else:
    small = []
    big = []
    for _ in range(n - 1):
        s, b = map(int, input().split())
        small.append(s)
        big.append(b)
    k = int(input())

    # 징검다리 번호는 0부터 시작
    # 매우 큰 점프를 안 할 때
    dp = [0] * n  # n 번째 칸에 n 번째 까지 가는 에너지 저장 (0 ~
    dp[1] = small[0]
    for i in range(2, n):
        dp[i] = min(dp[i - 2] + big[i - 2], dp[i - 1] + small[i - 1])
    energy = dp[-1]

    # 매우 큰 점프를 할 때
    dp2 = dp[:]
    for i in range(3, n):  # 처음부터 매우 큰 점프를 하면 3번 징검다리로 넘어가니까 3부터
        if dp[i - 3] + k >= dp[i]:  # 만약 큰 점프를 했는데 이전에 있던 최소값보다 크면 계산x
            continue
        dp2[i] = dp[i - 3] + k                  # 큰 점프를 했을 경우의 dp 다시 계산
        for j in range(i+1, n):
            dp2[j] = min(dp2[j - 2] + big[j - 2], dp2[j - 1] + small[j - 1], dp[j])
        energy = min(energy, dp2[-1])

    print(energy)
