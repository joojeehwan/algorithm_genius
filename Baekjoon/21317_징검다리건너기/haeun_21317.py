"""
https://velog.io/@swbest99/%EB%B0%B1%EC%A4%80-21317-%EC%A7%95%EA%B2%80%EB%8B%A4%EB%A6%AC-%EA%B1%B4%EB%84%88%EA%B8%B0
"""

N = int(input())

if N == 1:
    print(0)
elif N == 2:
    small, big = map(int, input().split())
    print(small)
else:
    small, big = [0] * (N - 1), [0] * (N - 1)

    for i in range(N - 1):
        small[i], big[i] = map(int, input().split())

    dp = [0] * N

    K = int(input())

    dp[1], dp[2] = small[0], min(small[0]+small[1], big[0])

    for j in range(3, N):
        dp[j] = min(dp[j-2]+big[j-2], dp[j-1]+small[j-1])

    energy = dp[N-1]
    copy_dp = dp[:]

    # 한 칸씩 매우 큰 점프 시도
    for i in range(N-3):
        if dp[i] + K < dp[i+3]:
            copy_dp[i+3] = dp[i] + K
            # 매우 큰 점프 했으니 3 칸 뒤부터 재 계산
            for j in range(i+4, N):
                # 원래 계산했던 값, 이전에 작은 점프 값, 큰 점프 값
                copy_dp[j] = min(dp[j], copy_dp[j-1] + small[j-1], copy_dp[j-2] + big[j-2])
            # 총 에너지가 더 값이 줄었는가 본다.
            if copy_dp[N-1] < energy:
                energy = copy_dp[N-1]
    print(energy)