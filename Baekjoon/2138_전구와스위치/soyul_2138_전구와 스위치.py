import sys

n = int(sys.stdin.readline())
bulbs = list(map(int, sys.stdin.readline().rstrip()))
bulbs2 = bulbs[:]
result = list(map(int, sys.stdin.readline().rstrip()))
ans1, ans2 = 2 * n, 2 * n


# 첫번쨰를 켜는 경우
cnt = 1
bulbs[0] = (bulbs[0] + 1) % 2
bulbs[1] = (bulbs[1] + 1) % 2

# 1번인덱스부터 검사
# 내 앞 전구가 결과와 다르면 스위치
for i in range(1, n-1):
    if bulbs[i-1] != result[i-1]:
        cnt += 1
        bulbs[i-1] = (bulbs[i-1] + 1) % 2
        bulbs[i] = (bulbs[i] + 1) % 2
        bulbs[i+1] = (bulbs[i+1] + 1) % 2

# 마지막 n번째 전구는 따로 검사
if bulbs[n-2] != result[n-2]:
    cnt += 1
    bulbs[n-2] = (bulbs[n-2] + 1) % 2
    bulbs[n-1] = (bulbs[n-1] + 1) % 2

# 결과는 마지막 두개만 검사
if bulbs[-2] == result[-2] and bulbs[-1] == result[-1]:
    ans1 = cnt

# 첫번째를 켜지 않는 경우
cnt2 = 0

# 1번인덱스부터 검사
# 내 앞 전구가 결과와 다르면 스위치
for i in range(1, n-1):
    if bulbs2[i-1] != result[i-1]:
        cnt2 += 1
        bulbs2[i-1] = (bulbs2[i-1] + 1) % 2
        bulbs2[i] = (bulbs2[i] + 1) % 2
        bulbs2[i+1] = (bulbs2[i+1] + 1) % 2

if bulbs2[n-2] != result[n-2]:
    cnt2 += 1
    bulbs2[n-2] = (bulbs2[n-2] + 1) % 2
    bulbs2[n-1] = (bulbs2[n-1] + 1) % 2

if bulbs2[-2] == result[-2] and bulbs2[-1] == result[-1]:
    ans2 = cnt2

# 만약에 정답이 갱신되지 않았다면 답이 없다는 뜻
if ans1 == 2 * n and ans2 == 2 * n:
    print(-1)
else:
    print(min(ans1, ans2))
