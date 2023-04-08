size = int(input())  # 수열 크기
arr = list(map(int, input().split()))  # 수열

dp = []
for num in arr:
    if not dp or dp[-1] < num:  # 가장 큰 수 = 수열의 가장 뒤
        dp.append(num)
    else:  # 가장 크지 않은 수 = 나와 가장 가까운 수들 사이에 삽입 = 나보다 큰 수 중 가장 작은 수와 교환
        start, end = 0, len(dp) - 1
        while start <= end:
            center = (start + end) // 2
            if dp[center] > num:
                end = center - 1
            elif dp[center] < num:
                start = center + 1
                center = start
            else:
                break
        dp[center] = num


print(len(dp))