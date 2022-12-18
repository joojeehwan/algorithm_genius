'''

이분탐색


무엇을 대상으로 하는가?!


가장 긴 증가하는 부분 수열을 구해야 함.

LIS?!(최장 증가 부분 수열)



1. res에 배열의 첫번째 값을 넣어줍니다.

2. for문으로 배열의 끝까지 검사를 하게 되는데
2-1. res에서 가장 큰 값보다 arr[i]가 더 크다면 그대로 res에 append해줍니다.
2-2. 아니라면 res 배열에서 해당하는 숫자가 있는지 이분탐색으로 찾아보고 res[index]에 arr[i]를 넣어줍니다.

3. res의 길이를 출력합니다.
'''

# 풀이 1

n = int(input())
arr = list(map(int, input().split(" ")))


def binary_search(start, end, target):
    if start > end:
        return start

    mid = (start + end) // 2

    if res[mid] > target:
        return binary_search(start, mid - 1, target)
    elif res[mid] == target:
        return mid
    else:
        return binary_search(mid + 1, end, target)


res = [arr[0]]

for i in range(1, len(arr)):
    if res[-1] < arr[i]:
        res.append(arr[i])
    else:
        res[binary_search(0, len(res) - 1, arr[i])] = arr[i]

print(len(res))


# 풀이 2

N = int(input())
A = list(map(int, input().split()))
LIS = [A[0]]

# 1
for n in A[1:]:
    # 2
    if LIS[-1] < n:
        LIS.append(n)
    else:  # 3
        left = 0
        right = len(LIS) - 1

        # 4
        while left < right:
            mid = (left + right) // 2

            if LIS[mid] < n:
                left = mid + 1
            else:
                right = mid

        LIS[right] = n

print(len(LIS))


#풀이 3

from bisect import bisect_left #이진탐색 코드, 같은 수일 경우 왼쪽 index를 돌려준다

input()
A = list(map(int, input().split()))
dp = []

for i in A:
    k = bisect_left(dp, i) #자신이 들어갈 위치 k
    if len(dp) <= k: #i가 가장 큰 숫자라면
        dp.append(i)
    else:
        dp[k] = i #자신보다 큰 수 중 최솟값과 대체
print(len(dp))