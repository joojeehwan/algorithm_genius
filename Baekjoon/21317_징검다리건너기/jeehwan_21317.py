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