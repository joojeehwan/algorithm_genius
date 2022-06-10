# def solution(money):
#     dp1 = [0] * len(money)
#     dp1[0] = money[0]
#     dp1[1] = max(money[0], money[1])

#     for i in range(2, len(money)-1): # 첫 집을 무조건 터는 경우
#         dp1[i] = max(dp1[i-1], money[i]+dp1[i-2])

#     dp2 = [0] * len(money)
#     dp2[0] = 0
#     dp2[1] = money[1]

#     for i in range(2, len(money)): # 마지막 집을 무조건 터는 경우
#         dp2[i] = max(dp2[i-1], money[i]+dp2[i-2])

#     return max(max(dp1), max(dp2)) # 두 경우 중 최대


def solution(money):
    answer = 0
    n = len(money)

    # dp1 : 첫번쨰 집은 무조건 텀, 마지막 집 안 텀
    # dp2 : 첫번쨰 집 무조건 안 텀, 마지막 집 텀

    dp1 = [0] * n
    dp2 = [0] * n

    # dp1은 "무조건" 첫번쨰 집을 터는 경우이므로! dp1[0]과 dp1[1]dp money[0]을 넣어준다.
    dp1[0] = dp1[1] = money[0]

    # dp2는 첫번째 집을 털지 않으므로 dp2[0]에 그대로 0을 넣어주고 dp2[1]에는 money[1]
    # dp2[2]에 money[1]과 money[2] 중 큰 값을 넣어준다.
    dp2[1] = money[1]
    dp2[2] = max(money[1], money[2])

    for i in range(2, n - 1):  # 어차피 마지막 집을 못터니깐! n-2까찌만 본다
        dp1[i] = max(dp1[i - 1], dp1[i - 2] + money[i])

    # dp2는 마지막 집 까찌도 털 수 있으니깐! 반복문을 n-1 까지 돌리는군
    for i in range(2, n):
        dp2[i] = max(dp2[i - 1], dp2[i - 2] + money[i])

    return max(dp1[n - 2], dp2[n - 1])


