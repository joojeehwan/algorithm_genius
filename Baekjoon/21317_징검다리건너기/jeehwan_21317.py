'''

점프를 하는 돌의 번호마다, 에너지 소비가 다르다?! 뭐지..?!


2가지의 풀이가 가능

dfs 풀이

dp 풀이

아래 풀이 수정해서 내것으로 만들기


'''

import sys
input = sys.stdin.readline
n = int(input())
info = [[0, 0] for _ in range(20)]
dp = [[10**5, 10**5] for _ in range(20)]
for i in range(n-1):
    info[i][0], info[i][1] = map(int, input().split())
k = int(input())

dp[0][0] = dp[0][1] = 0
dp[1][0] = info[0][0]
dp[2][0] = min(dp[0][0] + info[0][1], dp[1][0] + info[1][0])
for i in range(3, n):
    for j in range(2):
        dp[i][j] = min(dp[i-1][j]+info[i-1][0], dp[i][j])
        dp[i][j] = min(dp[i-2][j]+info[i-2][1], dp[i][j])
    dp[i][1] = min(dp[i][1], dp[i-3][0]+k)

print(min(dp[n-1][0], dp[n-1][1]))

import sys
input = sys.stdin.readline




N = int(input())
stone = []


#dp 배열 생성

dp = [1e9] * N
dp[0] = 0

#매우 큰 점프 없이,작은점프, 큰점프 만을 이용해서 실행해보기!
for i in range(N-1):

    j1, j2 = map(int, input().split())
    stone.append((j1, j2))

    if i + 1 < N:
        dp[i+1] = min(dp[i+1], dp[i] + j1)

    if i + 2 < N:
        dp[i+2] = min(dp[i+2], dp[i] + j2)


#매우 큰 점프를 적용해보기!

K = int(input())

MIN = dp[-1]

for i in range(3, N):
    e, dp1, dp2 = dp[i-3] + K , 1e9, 1e9
    for j in range(i, N-1):
        if i + 1 <= N:
            dp1 = min(dp1, e + stone[j][0])
        if i + 2 <= N:
            dp2 = min(dp2, e + stone[j][1])
        e, dp1, dp2 = dp1, dp2, 1e9

    MIN = min(MIN, e)

print(MIN)



n = int(input())
arr = []
for _ in range(n-1):
    arr.append(list(map(int, input().split())))
k = int(input())

ans = 10**9
def dfs(isK, idx, sum):
    global ans
    if sum >= ans or idx >= n:
        return
    if idx == n-1:
        ans = min(ans, sum)
        return
    dfs(isK, idx+1, sum+arr[idx][0])
    dfs(isK, idx+2, sum+arr[idx][1])
    if not isK:
        dfs(True, idx+3, sum+k)

dfs(False, 0, 0)
print(ans)

# global ans
# ans = int(1e9)
#
# N = int(input())
# arr = [list(map(int, input().split())) for _ in range(N - 1)]
# K = int(input())
#
#
# def dfs(idx, cost, status):
#     global ans
#     if idx == N - 1:
#         if ans > cost:
#             ans = cost
#         return
#
#     if idx + 1 < N:
#         dfs(idx + 1, cost + arr[idx][0], status)
#     if idx + 2 < N:
#         dfs(idx + 2, cost + arr[idx][1], status)
#     if idx + 3 < N and status:
#         dfs(idx + 3, cost + K, False)
#
#
# dfs(0, 0, True)
# print(ans)
global ans
ans = int(1e9)


N = int(input())
arr = [list(map(int, input().split())) for _ in range(N - 1)]
k = int(input())

def dfs(lev, cost, status):

    global ans

    if lev == N - 1:
        #최솟값 찾는 로직
        if ans > cost:
            ans = cost
        return

    dfs(lev + 1, cost + arr[lev][0], status)
    dfs(lev + 2, cost + arr[lev][1], status)

    if lev + 3 < N and status:
        dfs(lev + 3, cost + K, False)

dfs(0, 0, True)
print(ans)

