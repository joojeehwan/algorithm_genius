'''


dp의 바이블

k무게 만큼 가방에 넣을 수 있음.

각각의 무게 w에 맞는 가치 v가 할당됨.

v만큼 준서는 행복할 수 있음.

최대한 즐거운 여행을 하기 위해서, 배낭에 넣을 수 있는 물건들의 가치의 최댓값 구하기



냅색 알고리즘

'''



# from collections import defaultdict
#
# N, W = map(int, input().split())
#
#
# dit = defaultdict(int)
#
# for _ in range(N):
#     W, V = map(int, input().split())
#     dit[W] = V

n, k = map(int, input().split())
lst=[[0, 0]]
for _ in range(n):
    lst.append(list(map(int, input().split())))
dp = [[0]*(k+1) for _ in range(n+1)]
for i in range(1, n+1):
    for j in range(1, k+1):
        weight = lst[i][0]
        value = lst[i][1]
        if j < weight:  # 가방에 넣을 수 없으면
            dp[i][j] = dp[i - 1][j]  # 위에 값 그대로 가져오기
        else: # 가방에 넣을 수 있으면
            dp[i][j] = max(dp[i - 1][j], dp[i][j - weight] + value)
print(dp[n][k])

'''
입력
4 7
6 13
4 8
3 6
5 12

출력
14
