def solution(money):

    # 맨 앞에 집을 터는 경우 초기설정
    dp = [0] * len(money)
    dp[0] = money[0]
    dp[1] = max(money[0], money[1])

    for i in range(2, len(money)-1):                # 맨 마지막 집은 안털거니까 -1 까지
        dp[i] = max(dp[i-1], dp[i-2] + money[i])

    # 맨 마지막 집을 터는 경우 초기설정 (0번째 집은 안텀)
    dp2 = [0] * len(money)
    dp2[1] = money[1]

    for j in range(2, len(money)):
        dp2[j] = max(dp2[j-1], dp2[j-2] + money[j])

    answer = max(max(dp), max(dp2))
    return answer

print(solution([1, 2, 3, 1]))
