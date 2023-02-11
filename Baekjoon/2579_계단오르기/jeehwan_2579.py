'''



1. 계단은 한 번에 한 계단씩 또는 두 계단씩 오를 수 있다. 즉, 한 계단을 밟으면서 이어서 다음 계단이나, 다음 다음 계단으로 오를 수 있다.

2. 연속된 세 개의 계단을 모두 밟아서는 안 된다. 단, 시작점은 계단에 포함되지 않는다.

3. 마지막 도착 계단은 반드시 밟아야 한다.

총 점수의 최댓값을 구해야 한다.



마지막 도착점에 도착하기 위해서 잘 생각해보면,

마지막 도착 계단 전에 계단을 밝고 오는 경우와

마지막 도착 계단 전에 계닫을 밝지 않고, 2칸전에서 오는 경우가 있을 수 있음

그런데 3개의 계단을 연속으로 갈 수 없는 조건도 생각해야 하기 떄문에


ex) dp[3]의 경우

dp[3] = max(dp[1] + stair[3], dp[0] + stair[2] + stair[3])
'''

N = int(input())

stair = [0] * (N + 1)

for i in range(1, N + 1):
    stair[i] = int(input())

DP = [0] * (N + 1)


# 예외 처리를 해주지 않으면, 인덱스 에러난다...!
if N == 1:
    print(stair[N])

elif N == 2:
    print(stair[1] + stair[2])

else :
    DP[1] = stair[1]
    DP[2] = stair[1] + stair[2]
    DP[3] = max(stair[2] + stair[3], stair[1] + stair[3])

    for i in range(4, N + 1):
        # 3개 연속 밝으면 안된다.

        DP[i] = max(DP[i-3] + stair[i-1] + stair[i], DP[i-2] + stair[i])

    print(DP[N])
