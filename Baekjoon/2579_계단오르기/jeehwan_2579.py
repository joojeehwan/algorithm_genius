'''



1. 계단은 한 번에 한 계단씩 또는 두 계단씩 오를 수 있다. 즉, 한 계단을 밟으면서 이어서 다음 계단이나, 다음 다음 계단으로 오를 수 있다.

2. 연속된 세 개의 계단을 모두 밟아서는 안 된다. 단, 시작점은 계단에 포함되지 않는다.

3. 마지막 도착 계단은 반드시 밟아야 한다.

총 점수의 최댓값을 구해야 한다.




'''

N = int(input())

stair = [0] * 301

for i in range(N):
    stair[i] = int(input())



DP = [0] * 301
DP[0] = stair[0]
DP[1] = stair[0] + stair[1]
DP[2] = max(stair[0] + stair[2], stair[1] + stair[2])


for i in range(3, N):
    DP[i] = max(DP[i-3] + stair[i-1] + stair[i], DP[i-2] + stair[i])